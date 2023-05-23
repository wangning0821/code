class ListQueue:
    def __init__(self,MaxSize):
        self.MaxSize = MaxSize
        self.s = [0] * MaxSize
        self.front = -1
        self.fear = -1

    def addQ(self, item):
        if self.front - self.fear== self.MaxSize:
            return 'full'
        else:
            self.front = (self.front + 1) % self.MaxSize
            self.s[self.front] = item
        #print(self.t,self.n-1)
    def isempty(self):
        return self.front == self.fear
    def deleteQ(self):
        if self.isempty():
            return ('cant delete')
        self.fear = (self.fear + 1) % self.MaxSize

if __name__=='__main__':
    queue = ListQueue(3)
    print(queue.addQ(1), 1)
    print(queue.addQ(2), 2)
    print(queue.addQ(3), 3)
    print(queue.s)
    print(queue.deleteQ(), 3)
    print(queue.addQ(4), 4)
    print(queue.s)
