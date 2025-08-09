new_list = int(input("enter the number"))
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print(evens)
numbers = [1, 2, 3, 4, 5]
status = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(status)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
print(flattened)