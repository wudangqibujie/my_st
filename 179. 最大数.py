class Solution:
    def largestNumber(self, nums):
        nums = [str(i) for i in nums]

        def resort(lst):
            if len(lst) < 2:
                return lst

            log = [[] for _ in range(10)]
            for i in lst:
                log[int(i[0])].append(i)

            rslt = []
            for sub_lst in log:
                # print("sublist", sub_lst)
                if len(sub_lst) > 1:
                    new_lst = []
                    sing_flags = []
                    for s_i in sub_lst:
                        if len(s_i) > 1:
                            new_lst.append(s_i[1: ])
                        else:
                            sing_flags.append(s_i[0])
                    if len(new_lst) < 1 and len(sing_flags) < 1:
                        continue
                    res = resort(new_lst)
                    # print("singlist: ", sing_flags)
                    if len(sing_flags) >= 1:
                        sing_flag = sing_flags[0]
                        kx = 0
                        while kx < len(res) and int(res[kx][-1]) < int(sing_flag):
                            kx += 1
                        # print("debu: ", res, kx)

                        if kx == len(res):
                            res.extend(['' for _ in range(len(sing_flags))])
                        else:
                            # print("debu: ", res)
                            res = res[: kx] + ['' for _ in range(len(sing_flags))] + res[kx: ]
                    # else:

                    # print(res)
                    # print("RESS:", [f"{s_i[0]}{i}" for i in res])
                    rslt.extend([f"{s_i[0]}{i}" for i in res])
                else:
                    rslt.extend(sub_lst)
            return rslt
        rslt = resort(nums)
        rslt.reverse()
        print(rslt)
        return "".join(rslt)


s = Solution()
nums = [22, 51, 55, 56, 5, 0, 667, 66, 123, 6, 66]
nums = [10, 2]
nums = [3,30,34,5,9]
nums = [0, 1]
nums = [0, 21, 10, 10]
# nums = [3,30,34,5,9]
nums = [34323, 3432]
print(nums)
print(s.largestNumber(nums))

"343234323"
"343233432"