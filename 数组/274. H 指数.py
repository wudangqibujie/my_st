class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        # print(citations)

        ix = 1
        rs = 0
        while ix <= len(citations):
            # print(citations[-ix])
            if ix >= citations[-ix]:
                rs = max(rs, citations[-ix])
            ix += 1

        return rs


s = Solution()
citations = [3,0,6,1,5]
citations = [1,3,1]
citations = [0, 1, 3, 4, 5, 6, 8]
citations = [2]
print(s.hIndex(citations))