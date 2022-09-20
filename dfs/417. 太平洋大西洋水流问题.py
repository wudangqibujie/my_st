# class Solution(object):
#     def pacificAtlantic(self, heights):
#         """
#         :type heights: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         dp = [[[0, 0] for _ in range(len(heights[0]))] for _ in range(len(heights))]
#
#         def search(i, j, height):
#             print(i, j)
#             if readed[i][j]:
#
#             if i == -1 or j == -1:
#                 return [1, 0]
#             if i == len(heights)or j == len(heights[0]):
#                 return [0, 1]
#             if heights[i][j] > height:
#                 return [0, 0]
#             if dp[i][j][0]:
#                 return [1, 0]
#             if dp[i][j][1]:
#                 return [0, 1]
#             rs1 = search(i - 1, j, heights[i][j])
#             rs2 = search(i + 1, j, heights[i][j])
#             rs3 = search(i, j - 1, heights[i][j])
#             rs4 = search(i, j + 1, heights[i][j])
#             rs = [rs1, rs2, rs3, rs4]
#             rs_up = [i[0] for i in rs]
#             rs_lo = [i[1] for i in rs]
#             dp[i][j] = [int(1 in rs_up), int(1 in rs_lo)]
#             return dp[i][j]
#
#         for i in range(len(heights)):
#             for j in range(len(heights[0])):
#                 readed = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
#                 search(i, j, heights[i][j])
#
#
# s = Solution()
# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# s.pacificAtlantic(heights)
#
#
