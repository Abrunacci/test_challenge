"""
=====================
Title: Cycle Length
=====================

Problem:

Consider a list of integers “arr”, for example [2, 0, 1, 4, 3, 5].

Given an index, (e.g 0), move on to arr[0] (i.e 2 in the example above).
Now move to arr[2]. Repeating that can be done indefinitely.
A cycle occurs when a move returns to an already visited index.

Your task is to write a function
`cycle_length(arr: List[int], start_index: int) -> int`,
which will return the length of the cycle if found, given a starting index,
else return -1.

Function signature: cycle_length(indices: List[int], start_index: int) -> int

Inputs:

- arr: A list of integers.
- start_index: An integer representing the starting index.

Outputs:

- Return an integer representing the length of the cycle if found.
  If no cycle found, return -1.

Example:

cycle_length([2, 0, 1, 4, 3, 5], 0) should return 3 because if we start at 0
we go to 2 -> 1 -> 0 which forms a cycle of length 3.
"""
from typing import List


def cycle_length(arr: List[int], start_index: int) -> int:
    counter = 0
    visited_index = []
    next_index = arr[start_index]
    loop = True
    while loop:
        counter += 1
        visited_index.append(next_index)
        if next_index > len(arr) - 1:
            counter = -1
            break
        next_index = arr[next_index]
        if next_index in visited_index:
            break
    return counter if counter != 0 else -1