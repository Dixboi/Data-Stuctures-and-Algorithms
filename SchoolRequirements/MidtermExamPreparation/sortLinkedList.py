class Node():
    
    def __init__(self, data = None):
        self.data = data
        self.next_node = None
        
class LinkedList():
    
    def __init__(self):
        self.head = Node()
        self.tail = None
        self.head.next_node = self.tail
        
    def add(self, data):
        new_node = Node(data)
        
        #if list is empty
        if self.head.next_node == None:
            current_node = self.head
            self.tail = new_node
            current_node.next_node = self.tail
        #if list is not empty
        else:
            #if new_node has the largest value
            if new_node.data > self.tail.data:
                current_node = self.tail
                self.tail = new_node
                current_node.next_node = self.tail
            #if new_node is smallest or in between
            else:
                current_node = self.head
                
                while current_node.next_node.data < new_node.data:
                    current_node = current_node.next_node
                    
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
        
    def display(self):
        current_node = self.head
        
        while current_node.next_node != None:
            current_node = current_node.next_node
            print(current_node.data)

string = "the quick brown fox jumps over the lazy dog"
ll = LinkedList()

for i in string.split():
    ll.add(i)

ll.display()
