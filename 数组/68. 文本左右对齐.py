class Solution:
    def fullJustify(self, words, maxWidth):
        def aligh(left_lenght, space_num, coll):
            if left_lenght == 0 or space_num == 0:
                return [" " * i for i in coll]
            # print(left_lenght, space_num)
            rs = left_lenght // space_num + 1 if left_lenght % space_num != 0 else left_lenght // space_num
            coll.append(rs)
            left_lenght -= rs
            space_num -= 1
            return aligh(left_lenght, space_num, coll)


        rslt = []
        ix = 0
        chunk = []
        chunk_length = 0
        while ix < len(words):
            if len(words[ix]) + chunk_length + len(chunk) - 1 >= maxWidth:
                # print("START", maxWidth - chunk_length, len(chunk) - 1)
                # print(chunk)
                spacenums = aligh(maxWidth - chunk_length, len(chunk) - 1, [])
                s = ''
                if spacenums:
                    for jx, j in enumerate(chunk):
                        s += j
                        if jx != len(chunk) - 1:
                            s += spacenums[jx]
                else:
                    s = chunk[0] + " " * (maxWidth - len(chunk[0]))
                rslt.append(s)
                chunk = []
                chunk_length = 0
                continue
            chunk.append(words[ix])
            chunk_length += len(words[ix])
            ix += 1
        if chunk:
            lst_s = " ".join(chunk)
            lst_s += " " * (maxWidth - len(lst_s))
            rslt.append(lst_s)
        # for i in rslt:
        #     print(f"**{i}**")
        return rslt


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20

solution = Solution()
solution.fullJustify(words, maxWidth)
print(len("everything  else  we"))


