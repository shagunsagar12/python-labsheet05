tuple1 = (10, 20, 30)
tuple2 = (1, 2, 3)
result = tuple(a + b for a, b in zip(tuple1, tuple2))
print("Element-wise sum:", result)