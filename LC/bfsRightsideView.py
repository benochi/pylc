class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = deque()
        output = []

        if root:
            queue.append(root)

            while len(queue) > 0:
                lastNode = len(queue) - 1
                for i in range(len(queue)):
                    curr = queue.popleft()
                    if i == lastNode:
                        output.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

        return output
