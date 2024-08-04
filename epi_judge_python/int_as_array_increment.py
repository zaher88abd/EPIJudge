from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 0
    for i in reversed(range(len(A))):
        if A[i] != 9:
            A[i] += 1
            carry = 0
            break
        A[i] = 0
        carry = 1
    if carry == 1:
        A = [1] +A
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
