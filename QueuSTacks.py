class Queue(object):
    def __init__(self):
        self.Stack_1 = []
        self.Stack_2 = []
    def enqueue(self,v):
        self.Stack_1.append(v)
    def dequeue(self):
        if self.Stack_2:
            return self.Stack_2.pop()
        if self.Stack_1:
            while self.Stack_1:
                self.Stack_2.append(self.Stack_1.pop())
            return self.Stack_2.pop()
        return None        


#Driver function
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
#1234