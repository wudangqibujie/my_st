class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        dp = [[0 for _ in range(k)] for _ in range(k)]

        for i in range(len(nums2)):
            for j in range(len(nums1)):
                # print(i, j)
                if i >= len(dp) or j >= len(dp[0]):
                    continue
                dp[i][j] = nums1[j] + nums2[i]

        for i in dp:
            print(i)


s = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

nums1 = [1,1,3]
nums2 = [1,1,2]
k = 3

# nums1 = [1,2]
# nums2 = [3]
# k = 3
s.kSmallestPairs(nums1, nums2, k)

