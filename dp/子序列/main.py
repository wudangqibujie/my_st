# 首先，子序列问题本身就相对子串、子数组更困难一些，因为前者是不连续的序列，而后两者是连续的，就算穷举都不容易，更别说求解相关的算法问题了。

# 一旦涉及到子序列和最值，那几乎可以肯定，考察的是动态规划技巧，时间复杂度一般都是 O(n^2)。

# 既然要用动态规划，那就要定义 dp 数组，找状态转移关系。我们说的两种思路模板，就是 dp 数组的定义思路。不同的问题可能需要不同的 dp 数组定义来解决。

# 1、第一种思路模板是一个一维的 dp 数组：
# int n = array.length;
# int[] dp = new int[n];
#
# for (int i = 1; i < n; i++) {
#     for (int j = 0; j < i; j++) {
#         dp[i] = 最值(dp[i], dp[j] + ...)
#     }
# }

# 2、第二种思路模板是一个二维的 dp 数组：
# int n = arr.length;
# int[][] dp = new dp[n][n];
#
# for (int i = 0; i < n; i++) {
#     for (int j = 1; j < n; j++) {
#         if (arr[i] == arr[j])
#             dp[i][j] = dp[i][j] + ...
#         else
#             dp[i][j] = 最值(...)
#     }
# }
# 2.1 涉及两个字符串/数组时（比如最长公共子序列），dp 数组的含义如下：

# 在子数组arr1[0..i]和子数组arr2[0..j]中，我们要求的子序列（最长公共子序列）长度为dp[i][j]。
# 2.2 只涉及一个字符串/数组时（比如本文要讲的最长回文子序列），dp 数组的含义如下：

# 在子数组array[i..j]中，我们要求的子序列（最长回文子序列）的长度为dp[i][j]。

# 不知道大家做算法题有什么感觉，我总结出来做算法题的技巧就是，把大的问题细化到一个点，先研究在这个小的点上如何解决问题，然后再通过递归/迭代的方式扩展到整个问题。


