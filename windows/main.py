# int left = 0, right = 0;
#
# while (right < s.size()) {
#     // 增大窗口
#     window.add(s[right]);
#     right++;
#
#     while (window needs shrink) {
#         // 缩小窗口
#         window.remove(s[left]);
#         left++;
#     }
# }

# 适时保证维护一个状态信息的数据结构
