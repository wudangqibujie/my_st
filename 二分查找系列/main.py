# 另外声明一下，计算 mid 时需要防止溢出，代码中left + (right - left) / 2就和(left + right) / 2的结果相同，但是有效防止了left和right太大直接相加导致溢出。


def find(nums, target):
    i, j = 0, len(nums)

    while i < j:
        mid = int(i + (j - i) / 2)
        if target > nums[mid]:
            i = mid + 1
        elif target == nums[mid]:
            return True
        else:
            j = mid
    return False


# 查找最左边
def finf_leftset(nums, target):
    i, j = 0, len(nums)
    flag = False
    while i < j:
        mid = int(i + (j - i) / 2)
        if target > nums[mid]:
            i = mid + 1
        elif target == nums[mid]:
            flag = True
            break
        else:
            j = mid
    if not flag:
        return -1
    rs = mid
    ix, jx = 0, mid
    while ix < jx:
        midx = int(ix + (jx - ix) / 2)
        if target != nums[midx]:
            ix = midx + 1
        else:
            jx = midx
            rs = midx
    return rs

a = [2, 4]
print(finf_leftset(a, 3))