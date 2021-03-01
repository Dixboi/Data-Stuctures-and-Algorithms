lass Stack:
    
    #Constructor
    def __init__(self, stack = []):
        self.stack = stack
        
    #To add an item at the top
    def push(self, item = " "):
        self.stack.append(item)
        
    #To remove the top item
    def pop(self):
        self.stack.pop()
        
    #To count the number of items
    def count(self):
        return len(self.stack)
        
    #To know if the stack is empty or not
    def empty(self):
        return self.count() == 0
        
    #To know the top item
    def top(self):
        return self.stack[-1] if self.empty() == False else "No items"
        
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
        
if __name__ == "__main__":
    s1 = Stack()
    s2 = Stack([1, 2, 3])
    s1.details()
    s2.details()
