class Node():
    def __init__(self,data):
        self.head=data
        self.next=None

class LinkList():
    def __init__(self):
        self._head=None

    def is_empty(self):
        return self.head is None

if __name__ == "__main__":
    link_list = LinkList()
    node1 = Node(1)
    node2 = Node(2)
    link_list._head = node1
    node1.next = node2
    print(link_list._head.value)
    print(link_list._head.next.value)
    print(link_list.is_empty())
    #print(link_list.length())
