# 王宁
# 开发时间：2023/5/4 23:05
from LinearList import Mysqlist
from LinearList import LinkList,Node


class Liststack:
    def __init__(self, MaxSize):
        self.s = [0] * MaxSize
        self.top = -1
        self.MaxSize = MaxSize

    def isfull(self):
        return self.top == self.MaxSize - 1

    def push(self, item):
        if self.isfull():
            print('full')
        else:
            self.top += 1
            self.s[self.top] = item

    def isempty(self):
        return self.top == -1

    def stackpop(self):
        if self.top == -1:
            return None
        else:
            self.top -= 1
            res = self.s[self.top+1]
            self.s[self.top + 1] = 0
            return res


class Nodestack:
    def __init__(self,MaxSize):
        self.s = LinkList()
        self.top = -1
        self.MaxSize = MaxSize

    def isfull(self):
        return self.top == self.MaxSize - 1

    def push(self, item):
        if self.isfull():
            print('full')
        elif self.isempty():
            self.s._head = Node(item)
            self.top += 1
        else:
            new_node = Node(item)
            new_node.next = self.s._head
            self.s._head = new_node
            self.top += 1

    def isempty(self):
        return self.top == -1

    def stackpop(self):
        if self.top == -1:
            print('null')
        else:
            self.top -= 1
            current = self.s._head
            self.s._head = current.next
            return current.value


if __name__ == "__main__":
    a = Liststack(3)
    a.push(1)
    a.push(2)
    a.push(3)
    print(a.isfull())
    print(a.stackpop())
    print(a.stackpop())
    print(a.stackpop())
    print(a.stackpop())
    print(a.isempty())
    b = Nodestack(3)
    b.push(1)
    b.push(2)
    b.push(3)
    b.push(4)
    print(b.isfull())
    print(b.stackpop())
    print(b.stackpop())
    print(b.stackpop())
    print(b.stackpop())
