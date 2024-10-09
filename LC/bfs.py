from collections import deque

# O(n)


def bfs(root):
    queue = deque()

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_bfs():
    print("Test 1: Empty Tree")
    root = None
    bfs(root)
    # Expected output: nothing

    # Test 2: Single Node Tree
    print("\nTest 2: Single Node Tree")
    root = TreeNode(1)
    bfs(root)
    # Expected output:
    # level: 0
    # 1

    # Test 3: Simple Tree with 3 nodes
    print("\nTest 3: Simple Tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    bfs(root)
    # Expected output:
    # level: 0
    # 1
    # level: 1
    # 2
    # 3

    # Test 4: Larger Tree
    print("\nTest 4: Larger Tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    bfs(root)
    # Expected output:
    # level: 0
    # 1
    # level: 1
    # 2
    # 3
    # level: 2
    # 4
    # 5
    # 6

    # Test 5: Unbalanced Tree
    print("\nTest 5: Unbalanced Tree")
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    bfs(root)
    # Expected output:
    # level: 0
    # 1
    # level: 1
    # 2
    # level: 2
    # 3
    # level: 3
    # 4


# Run the tests
test_bfs()
