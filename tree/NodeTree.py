# 定义节点
class Node:
    # 初始化
    def __init__(self, value):
        # value存放数据元素
        self.value = value
        # next是下一个节点的标识
        self.left = None
        self.right = None

class LinkTree:
    def __init__(self):
        self._head = None
    def PreOrderTraversal(self):
        if self._head.left:
            print(self._head.left.PreOrderTraversal)
        return self._head.value

if __name__ == "__main__":
    link_tree = LinkTree()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    link_tree._head = node1
    node1.left = node2
    node1.right = node3
    print(link_tree._head.value)
    print(link_tree._head.left.value)
    print(link_tree._head.right.value)
    print(link_tree.PreOrderTraversal(),1111)