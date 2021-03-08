class Stack: # Stack class with a limit size
    
    #Constructor
    def __init__(self, size = 5):
        self.stack = []
        self.size = size
        
    #To count the number of items
    def count(self):
        return len(self.stack)
        
    #To know if the stack is empty or not
    def empty(self):
        return self.count() == 0
        
    #To know the top item
    def top(self):
        return self.stack[-1] if self.empty() == False else "No items"
        
    #To add an item at the top
    def push(self, item = " "):
        if self.size > self.count():
            self.stack.append(item)
        
    #To remove the top item
    def pop(self):
        if self.empty():
            self.stack.pop()
        
    #To display all the items from the top
    def items(self):
        if self.empty() == False:
            for item in range(len(self.stack) - 1, -1, -1):
                print(self.stack[item])
        else:
            print("No items to display.")
            
    #To display the details of the stack
    def details(self):
        print("Empty:", self.empty())
        print("Number of Items:", self.count())
        print("Top Item:", self.top())
        self.items()
