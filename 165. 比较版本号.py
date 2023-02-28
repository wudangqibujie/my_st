class Solution:
    def compareVersion(self, version1, version2):
        version1_lst = version1.split('.')
        version2_lst = version2.split('.')

        def clean_lst(version_lst):
            for ix in range(len(version_lst)):
                if version_lst[ix].startswith("0") and len(version_lst[ix]) > 1:
                    jx = 1
                    while jx < len(version_lst[ix]):
                        if version_lst[ix][jx] != "0":
                            break
                        jx += 1
                    rpl = version_lst[ix][jx: ] if jx != len(version_lst[ix]) else "0"

                    if not rpl:
                        rpl = "0"
                    version_lst[ix] = rpl
            return version_lst

        version1_lst = clean_lst(version1_lst)
        version2_lst = clean_lst(version2_lst)

        if len(version1_lst) > len(version2_lst):
            version2_lst.extend(['0' for _ in range(len(version1_lst) - len(version2_lst))])
        else:
            version1_lst.extend(['0' for _ in range(len(version2_lst) - len(version1_lst))])
        print(version1_lst)
        print(version2_lst)

        for ix in range(len(version1_lst)):
            if int(version1_lst[ix]) > int(version2_lst[ix]):
                return 1
            elif int(version1_lst[ix]) < int(version2_lst[ix]):
                return -1
        return 0


s = Solution()
# version1 = "1.01"
# version2 = "1.001"

# version1 = "1.0"
# version2 = "1.0.0"

# version1 = "0.1"
# version2 = "1.1"

version1 = "1.0.1.2"
version2 = "1.0.1"

# version1 = "1.00.1"
# version2 = "1.0.2"

# version1 = "1.1"
# version2 = "1.000000000000000000000010"
print(s.compareVersion(version1, version2))