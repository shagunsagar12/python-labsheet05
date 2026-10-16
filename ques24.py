tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
common = tuple(item for item in tuple1 if item in tuple2)
print("Common elements:", common)