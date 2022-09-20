class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        chr_ = {k: v for v, k in enumerate([chr(i) for i in range(97, 97 + 26)])}
        dp_bin = [[0 for _ in range(26)] for _ in range(len(words))]
        for ix, word in enumerate(words):
            for c in word:
                dp_bin[ix][chr_[c]] = 1
    
        # for i in dp_bin:
        #     print(i)
        cht = 0
        nums = [int(f"0b{''.join([str(i) for i in k])}", 2) for k in dp_bin]
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                ju = bin(nums[i] & nums[j])
                # print(words[i], words[j])
                if "1" in ju:
                    continue
                # count = bin(nums[i] ^ nums[j])
                # print(count)
                cht = max(cht, len(words[i]) * len(words[j]))
                # print(cht)
        return cht


# # print(bin(1101) ^ 1011)
# a = bin(100)
# b = bin(120)
# print(a)
# print(b)
# c = 100 ^ 120
# d = 100 & 120
# print(bin(c))
# print(bin(d))
#
# e = int('0b000010', 2)
# print(e)
#
# print({k: v for v, k in enumerate([chr(i) for i in range(97, 97 + 26)])})

s = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words = ["a","ab","abc","d","cd","bcd","abcd"]
words = ["a","aa","aaa","aaaa"]
print(s.maxProduct(words))