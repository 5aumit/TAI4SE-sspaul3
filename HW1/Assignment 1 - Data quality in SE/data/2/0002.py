from queue import Queue

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def array_to_tree_dfs(array):
    n = len(array)
    if n>0:
        root = Node(array[0])

    def dfs(node, index):
        # if index >= n:
        #     return
        # else:
        if 2*(index+1) -1 < n and array[2*(index+1) -1] is not None:
            node.left = Node(array[2*(index+1) -1])
            dfs(node.left, 2*(index+1) -1)
        if 2*(index+1) < n and array[2*(index+1)] is not None:
            node.right = Node(array[2*(index+1)])
            dfs(node.right, 2*(index+1))
        return
    dfs(root, 0)
    return root


def tree_to_array_bfs(root):
    q = Queue(maxsize = 0) # queue with infinity size
    q.put(root)
    array = []
    def bfs():
        if q.empty():
            return
        else:
            node = q.get()
            array.append(node.value)
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)
            bfs()
        return
    bfs()
    return array

            


def findClosestValueInBst(tree, target):
    distance = abs(tree.value - target)
    value = tree.value
    
    def dfs(node):
        nonlocal distance, value
        # stop condition
        if(node is None):
            return value
        if(node.value == target):
            return target

        if abs(node.value - target) < distance:
            value = node.value
            distance = abs(value - target)

        # recursion part
        if(node.value > target):
            return dfs(node.left)
        elif(node.value < target):
            return dfs(node.right)

    return dfs(tree)


if __name__ == '__main__':
    array = [5,3,10,2,4,8] + [None]*6 + [9] + [None]*2
    root = array_to_tree_dfs(array)
    new_array = tree_to_array_bfs(root) 
    print(new_array)
    print(findClosestValueInBst(root, 6))
    

