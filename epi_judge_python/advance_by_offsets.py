from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    reach_so_far, last_index = 0, len(A)
    index = 0
    while index <= reach_so_far and reach_so_far < last_index:
        reach_so_far = max(reach_so_far, A[index] + 1)
        index += 1
    return reach_so_far <= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
