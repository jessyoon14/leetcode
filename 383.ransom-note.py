#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    # using sort & two pointer
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = list(ransomNote)
        note.sort()
        mag = list(magazine)
        mag.sort()

        note_ptr = 0
        mag_ptr = 0
        while note_ptr < len(note) and mag_ptr < len(mag):
            note_char = note[note_ptr]
            mag_char = mag[mag_ptr]

            if note_char == mag_char:
                note_ptr += 1
                mag_ptr += 1
            elif note_char < mag_char:
                return False
            else:
                mag_ptr += 1

        return note_ptr == len(note)

#     # using sort & stacks
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         note = list(ransomNote)
#         note.sort(reverse=True)
#         mag = list(magazine)
#         mag.sort(reverse=True)

#         while note and mag:
#             note_char = note[-1]
#             mag_char = mag[-1]

#             if note_char == mag_char:
#                 note.pop()
#                 mag.pop()
#             elif note_char < mag_char:
#                 return False
#             else:
#                 mag.pop()

#         return len(note) == 0


#     # using collections
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(ransomeNote) > len(magazine):
#             return False

#         letters = collections.Counter(magazine)

#         for c in ransomNote:
#             if letters[c] <= 0
#                 return False
#             letters[c] -= 1
#         return True

#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # input validation (nonzero lengths)
#         if len(ransomNote) > len(magazine):
#             return False

#         # preprocess random note character frequency
#         chars = [0] * 26
#         for c in magazine:
#             c_idx = ord(c) - ord('a')
#             chars[c_idx] += 1

#         # magazine: decrement character frequency
#         for c in ransomNote:
#             c_idx = ord(c) - ord('a')
#             chars[c_idx] -= 1
#             if chars[c_idx] < 0:
#                 return False
#         return True


# @lc code=end
