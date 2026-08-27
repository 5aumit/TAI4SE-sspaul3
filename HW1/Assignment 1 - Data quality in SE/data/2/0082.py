class ListNode:
    def __init__(self,listt,node,g,h):
        self.node_list = []
        for element in listt:
            self.node_list.append(element)
        self.node_list.append(node)

        self.g=g
        self.f = int(g)+int(h);
        self.ID = node



    def is_Goal(self,complete_nodes):

        if complete_nodes in self.node_list:
            return True
        return False






