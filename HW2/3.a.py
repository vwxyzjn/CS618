import numpy as np
import itertools
s = np.array([
    [2,3,0,1],
    [3,2,1,0],
    [2,0,1,3],
    [3,1,0,2]
])

p = np.array([
    [2,3,1,0],
    [3,2,0,1],
    [2,0,1,3],
    [3,1,0,2]
])

n = len(s)
c = np.zeros_like(s)
for i in range(n):
    for j in range(n):
        r_ij = np.where(s[i] == j)[0][0]
        r_ji = np.where(p[j] == i)[0][0]
        c[i, j] = r_ij + r_ji


perms = itertools.permutations(range(n))

matchings = (10000000, None)
for perm in perms:
    indices = tuple(zip(range(n), perm))
    c_ij_sum = 0
    for item in indices:
        c_ij_sum += c[item]
    if c_ij_sum == matchings[0]:
        print(f"tie between {matchings} and {(c_ij_sum, indices)}")
    if c_ij_sum <= matchings[0]:
        matchings = (c_ij_sum, indices)

print(f"matching is {matchings}")

# calculate the utility for students
u = n - 1 - s
for m in matchings[1]:
    print(f"student {m[0]} has utility {u[m]}")
    