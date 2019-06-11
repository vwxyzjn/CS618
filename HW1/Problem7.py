# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:29:47 2019

@author: costa
"""
import numpy as np
import itertools

num_item = 4
num_agent = 4


v = np.array([
    {
        '[0, 0, 0, 0]': 0,
        '[1, 0, 0, 0]': 1,
        '[0, 1, 0, 0]': 2,
        '[0, 0, 1, 0]': 2,
        '[0, 0, 0, 1]': 4,
        '[1, 1, 1, 1]': 11,
        'else': 5
    },
    {
        '[0, 0, 0, 0]': 0,
        '[1, 0, 0, 0]': 1,
        '[0, 1, 0, 0]': 1,
        '[0, 0, 1, 0]': 1,
        '[1, 1, 0, 0]': 5,
        'else': 4
    },
    {
        '[0, 0, 0, 0]': 0,
        '[1, 0, 0, 0]': 1,
        '[0, 1, 0, 0]': 2,
        '[0, 0, 1, 0]': 4,
        '[0, 0, 0, 1]': 1,
        '[0, 1, 1, 0]': 7,
        'else': 3
    },
    {
        '[0, 0, 0, 0]': 0,
        '[1, 0, 0, 0]': 1,
        '[0, 1, 0, 0]': 1,
        '[0, 0, 1, 0]': 1,
        '[0, 0, 0, 1]': 3,
        'else': 3
    },
])

def utility(v, alloc):
    welfare = 0
    for idx, item in enumerate(alloc):
        item_string = str(item.tolist())
        if item_string in v[idx]:
            welfare += v[idx][item_string]
        else:
            welfare += v[idx]['else']
    
    return welfare

def allocation(v: np.array, num_item, num_agent):
    all_allocations = list(itertools.product([*list(itertools.product([0, 1], repeat=num_item))], repeat=num_agent))
    
    max_welfare = 0
    max_alloc = None
    
    for alloc in all_allocations:
        alloc = np.array(alloc)
        if np.count_nonzero(alloc.sum(axis=0) > 1) > 0:
            # a non-valid allocation
            continue
        welfare = utility(v, alloc)
        if welfare > max_welfare:
            max_welfare = welfare
            max_alloc = alloc
    
    return max_alloc, max_welfare

# calculate the payment
max_alloc, max_welfare = allocation(v, num_item, num_agent)
print(f"the maximum social is \n {max_welfare}")
print(f"the allocation is \n {max_alloc}")
for i, alloc in enumerate(max_alloc):
    print("==============================")
    if sum(alloc) != 0:
        max_a, max_w = allocation(v[np.arange(num_agent) != i], num_item, num_agent-1)
        print(f"max social welfare without agent {i} is \n {max_w}")
        print(f"allocation without agent {i} is \n {max_a}")
        print(f"payment for agent {i} is \n {max_w - utility(v[np.arange(num_agent) != i], max_alloc[np.arange(num_agent) != i])}")