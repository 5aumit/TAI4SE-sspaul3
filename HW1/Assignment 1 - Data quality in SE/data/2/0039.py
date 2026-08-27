class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        currentList = [root]
        nextList = []
        solution = []

        while currentList:
            thisLevel = [node.val for node in currentList]
            solution.append(thisLevel)
            for node in currentList:
                if node.left is not None:
                    nextList.append(node.left)
                if node.right is not None:
                    nextList.append(node.right)
            currentList, nextList = nextList, currentList
            del nextList[:]

        return solution
