def process_squares():
    try:
        start_range = int(input("Enter the starting number of the range: "))
        end_range = int(input("Enter the ending number of the range: "))
    except ValueError:
        print("Invalid input. Please enter integers for the range.")
        return
    all_squares = []
    odd_squares = []
    even_squares = []
    for num in range(start_range, end_range + 1):
        square = num * num
        all_squares.append(square)
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
    print(f"\nAll square values in the range [{start_range}, {end_range}]: {all_squares}")
    print(f"Odd square values: {odd_squares}")
    print(f"Even square values: {even_squares}")
process_squares()