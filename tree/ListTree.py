class ListTree:
    def __init__(self, res):
        self.tree = res
        self.n = len(res)
    def Left(self, s):
        if 2*s + 1 >= self.n:
            return
        return self.tree[2*s + 1]
    def Right(self, s):
        if 2*s + 2 >= self.n:
            return
        return self.tree[2*s + 2]
    def PreOrderTraversal(self,t=0):
        if t is None:
            return
        elif t >= self.n:
            return
        print(self.tree[t])
        self.PreOrderTraversal(2*t + 1)
        self.PreOrderTraversal(2*t + 2)
        return -1
    def InOrderTraversal(self, t=0):
        if t is None:
            return
        elif t >= self.n:
            return
        self.InOrderTraversal(2*t + 1)
        print(self.tree[t])
        self.InOrderTraversal(2*t + 2)
        return -1
    def PostOrderTraversal(self, t=0):
        if t is None:
            return
        elif t >= self.n:
            return
        self.PostOrderTraversal(2 * t + 1)
        self.PostOrderTraversal(2 * t + 2)
        print(self.tree[t])
        return -1
if __name__ == "__main__":
    t1 = ListTree([1,2,3,4,5])
    #print(t1.Left(0))
    print(t1.PreOrderTraversal())
    print('--------------------')
    print(t1.InOrderTraversal())
    print('--------------------')
    print(t1.PostOrderTraversal())
