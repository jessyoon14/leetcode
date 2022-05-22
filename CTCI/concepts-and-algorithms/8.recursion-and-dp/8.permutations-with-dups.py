'''
1) Create all possible permutations and rule out the duplicates
Do the same as 1, but collect into hashtable(set)
Time: O(n!) in all cases
Space: O(n!) (but needs additional memory for set)
- worst case: 
    - all characters same ('aaaa') -> still takes n! time
    - if long string with lots of unique char, waste of memory
- best case:
    - lots of repeated chars (set doesn't take too much space)

2) Generate only unique permutations
preprocess into dict, then do recursion
Pros: runs faster in cases with lots of duplicate characters

edge cases)
- all dups / no  dups / some dups
- multiple duplicates
- empty str

time: n! / (a! * b! * ... ) (a, b, ...: # of each nonunique char)
space: n! (since frequency table is constant space)
'''
from typing import List
from collections import Counter


def get_perms(s: str) -> List[str]:
    char_freq = Counter(s)
    result = []
    get_perms_rec('', char_freq, len(s), result)
    return result


def get_perms_rec(prefix, char_freq, remaining, result):
    # if all(value == 0 for value in char_freq.values()):
    #     result.append(prefix)
    if remaining == 0:
        result.append(prefix)
    for c in char_freq:
        if char_freq[c] > 0:
            char_freq[c] -= 1
            get_perms_rec(prefix + c, char_freq, result)
            char_freq[c] += 1


if __name__ == '__main__':
    print(get_perms('abcd'))
    print(get_perms('aabbcc'))
