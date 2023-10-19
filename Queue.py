
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,value):
        self.items.insert(0,value) 
    
    def dequeue(self):
        self.items.pop()

    def printqueue(self):
        return self.items


q = Queue()
q.enqueue("ali")
q.enqueue("roham")
q.enqueue("pinar")
print(q.printqueue())
print(type(q))
q.dequeue()
print(q.printqueue())

    
