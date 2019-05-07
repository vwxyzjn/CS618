# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:29:47 2019

@author: costa
"""
import numpy as np
import itertools

num_item = 4
num_agent = 4

np.zeros((4,4))

v = [
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
]

all_allocations = list(itertools.product([*list(itertools.product([0, 1], repeat=4))], repeat=4))

max_welfare = 0
max_alloc = None

for alloc in all_allocations:
    alloc = np.array(alloc)
    if np.count_nonzero(alloc.sum(axis=0) > 1) > 0:
        # a non-valid allocation
        continue
    welfare = 0

    for idx, item in enumerate(alloc):
        item_string = str(item.tolist())
        if item_string in v[idx]:
            welfare += v[idx][item_string]
        else:
            welfare += v[idx]['else']
    if welfare > max_welfare:
        max_welfare = welfare
        max_alloc = alloc
    