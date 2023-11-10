import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

listNumbers = []

for i in range(10000):
    # listNumbers.append(np.random.randint(10))
    # listNumbers.append(np.random.randint(10) + np.random.randint(10))
    listNumbers.append(
        np.random.randint(10) + np.random.randint(10) + np.random.randint(10)
    )
    # listNumbers.append(np.random.randint(10) + np.random.randint(10) + np.random.randint(10) + np.random.randint(10))
    # listNumbers.append(np.random.randint(10) + np.random.randint(10) + np.random.randint(10) + np.random.randint(10) + np.random.randint(10))
    pass

listNumbers = sorted(listNumbers)

count = {}

for elements in listNumbers:
    count[elements] = count.get(elements, 0) + 1

numbers = []
counts = []


for elements, cnt in count.items():
    numbers.append(str(elements))
    counts.append(cnt)


X = np.array([[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]])
Y = np.array([[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]])
Z = X + Y

for i in range(len(Z)):
    for j in range(len(Z[i])):
        if Z[i][j] in list(count.keys()):
            Z[i][j] = count[Z[i][j]]
        else:
            Z[i][j] = 0


fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="viridis")
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
ax.set_xlabel("Números X")
ax.set_ylabel("Números Y")
ax.set_zlabel("Vezes Repetidas Z")
plt.show()


fig = plt.figure(figsize=(10, 10))
# plt.bar(numbers, counts)
# plt.plot(numbers, counts)
plt.stackplot(numbers, counts)
plt.ylim(0)
plt.grid(color="#AAAAAA", linestyle="--", linewidth=0.5)
plt.ylabel("Vezes Repetidas")
plt.xlabel("Números")
plt.show()
