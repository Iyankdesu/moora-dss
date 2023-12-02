# import library
import numpy as np

# define alternative
alt = ["A1", "A2", "A3"]

# define decision matrix
matrix = np.array([
    [5, 3, 5, 5],
    [1, 3, 1, 1],
    [1, 5, 5, 2]
])

# criteria value
C1 = np.sqrt(np.sum(matrix[:, 0] ** 2))
C2 = np.sqrt(np.sum(matrix[:, 1] ** 2))
C3 = np.sqrt(np.sum(matrix[:, 2] ** 2))
C4 = np.sqrt(np.sum(matrix[:, 3] ** 2))

# normalize matrix
normalizedMatrix = np.zeros_like(matrix, dtype = float)
normalizedMatrix[:, 0] = matrix[:, 0] / C1
normalizedMatrix[:, 1] = matrix[:, 1] / C2
normalizedMatrix[:, 2] = matrix[:, 2] / C3
normalizedMatrix[:, 3] = matrix[:, 3] / C4

# print output
print("Decisions Matrix")
print(matrix)
print("\nCriteria Value")
print("C1 = ", C1)
print("C2 = ", C2)
print("C3 = ", C3)
print("C4 = ", C4)
print("\nNormalized Matrix")
print(normalizedMatrix)

# define weight value
W1 = 3
W2 = 2
W3 = 2
W4 = 3

# sum weight value
weights = W1 + W2 + W3 + W4

X = np.zeros_like(normalizedMatrix, dtype = float)
X[:, 0] = W1 * normalizedMatrix[:, 0] / weights
X[:, 1] = W2 * normalizedMatrix[:, 1] / weights
X[:, 2] = W3 * normalizedMatrix[:, 2] / weights
X[:, 3] = W4 * normalizedMatrix[:, 3] / weights

result = (X[:, 1] + X[:, 2]) - (X[:, 0] + X[:, 3])

# sort array
sortedIndices = np.argsort(result)[::-1]
print("\nAlternative Ranking")
for i, j in enumerate(sortedIndices):
  rank = i + 1
  print(f"Rank {rank}: {alt[j]} = {result[j]}")
