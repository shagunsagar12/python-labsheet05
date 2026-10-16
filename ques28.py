numbers = (1, 2, 3, 2, 4, 5, 1, 2)
repeated = tuple(item for item in dict.fromkeys(numbers) if numbers.count(item) > 1)
print("Repeated items:", repeated)

