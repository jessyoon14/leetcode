#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(line, line_length):
            num_spaces = maxWidth - line_length  # 20 - 18 = 2
            if len(line) < 2:
                line[0] = line[0] + " "*(num_spaces)
            else:
                num_spaces_per_slot = num_spaces // (len(line) - 1)  # 0
                num_spaces_left = num_spaces % (len(line) - 1)  # 2

                # add space to end of each word
                for i in range(len(line)-1):
                    num_spaces_curr = num_spaces_per_slot
                    if i < num_spaces_left:
                        num_spaces_curr += 1
                    line[i] = line[i] + " " * num_spaces_curr
            return " ".join(line)

        result = []
        line = [words[0]]  # store words in current line
        line_length = len(words[0])  # including 1 space in between

        for i in range(1, len(words)):
            word = words[i]
            # if new word does not cause overflow, fill line
            if line_length + len(word) + 1 <= maxWidth:
                line.append(word)
                line_length += len(word) + 1
            # if new word causes overflow, process current line (justify and add to result) and reset
            else:
                result.append(justify(line, line_length))  # 18
                line = [word]
                line_length = len(word)

        # adjust last line
        result.append(" ".join(line) + " " * (maxWidth - line_length))
        return result

# @lc code=end
