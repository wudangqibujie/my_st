class Solution:
    def findMinArrowShots(self, points):
        points = sorted(points, key=lambda item: item[1])
        print(points)
        cnt = 1
        st_interval = points[0]
        idx = 1
        while idx < len(points):
            st = points[idx][0]
            now_end = st_interval[1]
            if st > now_end:
                st_interval = points[idx]
                cnt += 1
            idx += 1
        return cnt





points = [[2,3],[2,3]]
s = Solution()
print(s.findMinArrowShots(points))