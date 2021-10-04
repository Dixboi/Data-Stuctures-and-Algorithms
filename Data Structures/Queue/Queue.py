
class Queue:
    
    def __init__(self, size = 5):
        self.size = size # size of the queue
        self.queue = []
    
    # Returns if the queue is full
    def isFull(self):
        return len(self.queue) == self.size
    
    # Returns if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
    
    # Returns the number of items of the queue
    def count(self):
        if self.isEmpty(): return 0
        if self.isFull(): return self.size
        return len(self.queue)
    
    # Adds an element on the first index
    def enqueue(self, item):
        if self.isFull() == False:
            self.queue.insert(0, item)
    
    # Removes the first inserted element
    def dequeue(self):
        if self.isEmpty() == False:
            self.queue.pop()
    
    # Return the first inserted element        
    def peek(self):
        if self.isEmpty(): return "Empty queue"
        return self.queue[-1]
    
    # Displays the details of the queue
    def details(self):
        print("Empty:", self.isEmpty())
        print("Full:", self.isFull())
        print("Current count:", self.count())
	print("First element: ", self.peek())
        print("Queue:")
        
        for i in self.queue:
            print(i, end = " ")
            
        print()
		
