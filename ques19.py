numbers = (1, 2, 2, 3, 4, 3, 5)
result = tuple(dict.fromkeys(numbers))
print("Tuple without duplicates:", result)