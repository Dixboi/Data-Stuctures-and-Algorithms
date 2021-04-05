# Initialization of the node
class Node():
    
    def __init__(self, data = None):
        self.data = data
        self.next_node = None

class LinkedList():
    
    def __init__(self):
        self.head = Node() #head of the linked list
        
	# Adding a new element to the end of the list
    def add(self, data):
        new_node = Node(data)
        current_node = self.head
        
        while current_node.next_node != None:
            current_node = current_node.next_node
            
        current_node.next_node = new_node
        
	# Displaying all elements of the list
    def display(self):
        current_node = self.head
        
        while current_node.next_node != None:
            current_node = current_node.next_node
            print(current_node.data, end = " ")
            
        print()
