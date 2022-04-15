def solution(lst):
    stack = []
    rs_idx = [None for _ in range(len(lst))]
    rs_val = [None for _ in range(len(lst))]
    ix = 0
    while ix < len(lst):
        i = lst[ix]
        while stack and stack[-1][-1] <= i:
            pop_idx, pop_val = stack.pop()
            # rs.append([pop_idx, pop_val, ix, i])  # 此时idx，此时值， 下一个大于自己的idx, 下一个大于自己的值
            rs_idx[pop_idx] = ix
            rs_val[pop_idx] = i
        stack.append((ix, i))
        ix += 1
        if ix == len(lst):
            while stack:
                pop_idx, pop_val = stack.pop()
                # rs.append([pop_idx, pop_val, -1, -1])
                rs_idx[pop_idx] = -1
                rs_val[pop_idx] = -1
    print(lst, "源")
    print(rs_idx, "IDX")
    print(rs_val, "VAL")
    cnt = 0
    readed = [False for _ in range(len(lst))]

    for ix in range(len(lst)):
        if lst[ix] == 0 or rs_idx[ix] == -1:
            continue
        if readed[ix]:
            cnt -= lst[ix]
        else:
            cnt += (rs_idx[ix] - ix - 1) * min(lst[ix], rs_val[ix])
            for j in range(ix, rs_idx[ix]):
                readed[j] = True
    print(cnt)
    return cnt



nums = [4,2,0,3,2,5]
solution(nums)
