# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:41:10 2019

@author: costa
"""

from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

A = 6.,4.,1.,7.,3.,2.,3.
B = 5.,1.,6.,4.,2.,3.,7.
L = ["A","B","C","D","E","F","G"]

plt.scatter(A,B)
for lxy in zip(L, A, B):                                       # <--
    ax.annotate('%s at (%s, %s)' % lxy, xy=(lxy[1],lxy[2]), textcoords='data')
plt.xlabel("agent 1's utility")
plt.ylabel("agent 2's utility")
plt.grid()
plt.savefig("2.svg")