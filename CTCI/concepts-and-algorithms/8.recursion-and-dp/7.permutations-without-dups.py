from typing import List

'''
Approah 1: building from permutations of the first n-1 characters
(build permutation of substring then insert new char into every possible position)

Time: O(n!) -> but I think it's O(n * n!), since there are n! possible permutations and each is length n (takes O(n) to build)
Space: O(n!) -> technically O(n * n!)

'''


def get_permutations1(s: str) -> List[str]:
    if len(s) < 2:
        return [s]

    perms = []
    tail_perms = get_permutations1(s[:-1])
    for tail_perm in tail_perms:  # O((n-1)!)
        for i in range(len(tail_perm) + 1):  # O(n)
            perm = tail_perm[:i] + s[-1] + tail_perm[i:]  # O(n)
            perms.append(perm)
    return perms


"""
Approach 2: building from permutations of all n-1 character substrings
fix prefix and compute permutation for the tail (can return list or do tail recursion)
                  5
   0        1          2       3         4
0 1 2 3   0 1 2 3   0 1 2 3  0 1 2 3   0 1 2 3

-> function gets called n! times (total of n! leaves in recursion tree)
-> each function call needs most n to run,  for str copy (ignore n recursive calls, since it's included in the # nodes calculation)
-> n * n!
"""


def get_permutations2(s: str) -> List[str]:
    if len(s) < 2:
        return [s]

    results = []

    for i in range(len(s)):
        permutations = get_permutations2(s[:i] + s[i+1:])
        for p in permutations:
            results.append(s[i] + p)

    return results


def get_permutations3(s: str) -> List[str]:
    result = []
    get_permutations_rec('', s, result)
    return result


def get_permutations_rec(prefix: str, remainder: str, result: List[str]):
    if not remainder:
        result.append(prefix)
        return

    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i + 1:]
        c = remainder[i]
        get_permutations_rec(prefix + c, before + after, result)
