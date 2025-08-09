test_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
target_value = 10
count = 0

for value in test_dict.values():
    if value == target_value:
        count += 1

print(f"The value {target_value} appears {count} times in the dictionary.")