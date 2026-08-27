class Node(object):

    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node=n


class LinkedList(object):

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        """
        To Add a new node or prepend a new node
        """
        new_node = Node(d)
        self.root = new_node
        self.size += 1
        return d

    def append(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_next() is None:
                this_node.set_next(Node(d))
                self.size += 1
                return d
            else:
                this_node=this_node.get_next()

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()

        return false

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return True
            else:
                this_node=this_node.get_next()
        return False


myList=LinkedList()
myList.add(1)
myList.append(2)
print myList.find(2)
print myList.get_size()
myList.remove(1)
print myList.find(2)
print myList.get_size()
