class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_huff_tree(nums):
    nums.sort(reverse=True)
    forest = [Node(i) for i in nums]
    while len(forest) > 1:
        pop_1 = forest.pop()
        pop_2 = forest.pop()
        new_node = Node(pop_1.val + pop_2.val)
        new_node.left = pop_1
        new_node.right = pop_2
        forest.append(new_node)
        ix2, ix1 = len(forest) - 1, len(forest) - 2
        while ix1 >= 0 and forest[ix2].val >= forest[ix1].val:
            forest[ix1], forest[ix2] = forest[ix2], forest[ix1]
            ix1 -= 1
            ix2 -= 1
    return forest[0]


nums = [4, 6, 3, 2]
rs = create_huff_tree(nums)
print(rs.val)
print(rs.left.val)
print(rs.right.val)
print(rs.right.left.val)
