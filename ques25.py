tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6)
difference = tuple(item for item in tuple1 if item not in tuple2)
print("Difference (tuple1 - tuple2):", difference)