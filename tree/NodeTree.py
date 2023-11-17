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
    def __init__(self, value):
        self._head = value

    def PreOrderTraversal(self):
        if self._head:
            print(self._head.value)
            LinkTree(self._head.left).PreOrderTraversal()
            LinkTree(self._head.right).PreOrderTraversal()
        else:
            return

    def InOrderTraversal(self):
        if self._head:
            LinkTree(self._head.left).InOrderTraversal()
            print(self._head.value)
            LinkTree(self._head.right).InOrderTraversal()
        else:
            return

    def PostOrderTraversal(self):
        if self._head:
            LinkTree(self._head.left).PostOrderTraversal()
            LinkTree(self._head.right).PostOrderTraversal()
            print(self._head.value)
        else:
            return


if __name__ == "__main__":
    #link_tree = LinkTree()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    node2.right = node6
    node3.left = node7

    link_tree = LinkTree(node1)
    link_tree.PreOrderTraversal()
    print('-------------')
    link_tree.InOrderTraversal()
    print('-------------')
    link_tree.PostOrderTraversal()
