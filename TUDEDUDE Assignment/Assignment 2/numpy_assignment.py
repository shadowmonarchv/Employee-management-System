import numpy as np
# 1. 1D Array operations
arr1d = np.arange(1, 21)
print(f"1D Array: {arr1d}")
print(f"Sum: {np.sum(arr1d)}, Mean: {np.mean(arr1d)}, Median: {np.median(arr1d)}, Std Dev: {np.std(arr1d):.2f}")

# Indices of elements > 10
indices = np.where(arr1d > 10)
print(f"Indices where elements > 10: {indices[0]}")

# 2. 2D Array (4x4)
arr2d = np.arange(1, 17).reshape(4, 4)
print(f"\n2D Array:\n{arr2d}")
print(f"Transpose:\n{arr2d.T}")
print(f"Row-wise sums: {np.sum(arr2d, axis=1)}")
print(f"Column-wise sums: {np.sum(arr2d, axis=0)}")

# 3. Random 3x3 Arrays
np.random.seed(42) # For reproducibility
rand1 = np.random.randint(1, 21, size=(3, 3))
rand2 = np.random.randint(1, 21, size=(3, 3))

print(f"\nAddition:\n{rand1 + rand2}")
print(f"Dot Product:\n{np.dot(rand1, rand2)}")

# 4. Reshaping and Slicing
arr12 = np.arange(1, 13)
reshaped = arr12.reshape(3, 4)
# Slice: first two rows ([0:2]), last two columns ([2:4] or [-2:])
sliced = reshaped[:2, -2:]
print(f"\nReshaped Array:\n{reshaped}")
print(f"Sliced Array (2x2):\n{sliced}")