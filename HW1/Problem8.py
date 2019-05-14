# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:29:47 2019

@author: costa
"""
import numpy as np
import itertools
import time
import random

all_n_m = list(itertools.product([2, 3, 4, 5], [2, 3, 4, 5]))

for (num_agent, num_item) in all_n_m:
    start = time.time()
    # generate values
    agent_possible_alloc = np.array(
        list(itertools.product([0, 1], repeat=num_item))
    )
    v = []
    for _ in range(num_agent):
        valuation = {}
        for item in agent_possible_alloc:
            valuation[str(item.tolist())] = random.uniform(0, 
                1) * item.sum()
        v += [valuation]

    all_allocations = itertools.product(
        [*list(itertools.product([0, 1], repeat=num_item))], 
        repeat=num_agent
    )

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
                welfare += v[idx]["else"]
        if welfare > max_welfare:
            max_welfare = welfare
            max_alloc = alloc

    print(f"n={num_agent}, m={num_item} takes ", time.time() - start)
    print(f"max_welfare={max_welfare}")
