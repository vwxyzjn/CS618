import numpy as np
import itertools

# true preferences
if True:
    s = np.array([
        [3,2,1,0],
        [0,2,1,3],
        [2,3,1,0],
        [3,2,1,0]
    ])
    n = len(s)
    # calculate the utility for students
    u = np.zeros_like(s)
    for i in range(n):
        for j in range(n):
            u[i, s[i,j]] =  n - j
    
    p = np.array([
        [0,3,1,2],
        [1,3,0,2],
        [2,3,1,0],
        [3,2,1,0]
    ])
    

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
            print("tie")
        if c_ij_sum <= matchings[0]:
            matchings = (c_ij_sum, indices)
    
    print(f"matching is {matchings}")
    

    for m in matchings[1]:
        print(f"student {m[0]} has utility {u[m]}")

# fake preferences
if True:
    s = np.array([
        [1,2,3,0],
        [0,2,1,3],
        [2,3,1,0],
        [3,2,1,0]
    ])
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
    
    print(f"untruthful matching is {matchings}")
    
    # calculate the utility for students
    for m in matchings[1]:
        print(f"student {m[0]} has utility {u[m]}")
