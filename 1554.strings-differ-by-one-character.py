class Solution:
    """
    Brute force
    time: O(n*m*m)
    space: O(n*m)
    edge
        - duplicates
        - no one-char diff
        - yes one-char diff
        - one word
        - two words
        - many words
        - word length 0
        - word length 1
    """

    def differByOne(self, dict: List[str]) -> bool:
        str_len = len(dict[0])
        word_count = len(dict)

        for i in range(str_len):
            seen = set()
            for word in dict:
                new_word = word[:i] + word[i + 1:]
                if new_word in seen:
                    return True
                seen.add(new_word)

        return False

    """
    String hashing
    """

    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        hashes = [0] * n
        MOD = 10**11 + 7

        # calculate hash for each word
        for i in range(n):
            for j in range(m):
                hashes[i] = (26*hashes[i] + (ord(dict[i][j]) - ord('a'))) % MOD

        base = 1
        for j in range(m-1, -1, -1):
            seen = set()
            for i in range(n):
                # hash without current char
                new_h = (hashes[i] - base * (ord(dict[i][j]) - ord('a'))) % MOD
                if new_h in seen:
                    return True
                seen.add(new_h)
            base = 26 * base % MOD
        return False
