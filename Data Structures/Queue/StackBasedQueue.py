#Initialization of the Queue
class StackQueue():
    
    def __init__(self):
        self.og_stack = []
        self.pl_stack = []
       
	#add elemenent to the stack
    def enqueue(self, data):
        #if og_stack is empty
        if len(self.og_stack) == 0:
            self.og_stack.append(data)
        #if og_stack is not empty
        else:
            for i in range(len(self.og_stack)):
                element = self.og_stack.pop()
                self.pl_stack.append(element)
                
            self.og_stack.append(data)
            
            for j in range(len(self.pl_stack)):
                element = self.pl_stack.pop()
                self.og_stack.append(element)
     
	#remove element from the stack
    def dequeue(self):
        #if og_stack is empty
        if len(self.og_stack) == 0:
            return
        #if og_stack is not empty
        else:
            self.og_stack.pop()
                
    def display(self):
        for data in self.og_stack[::-1]:
            print(data)
