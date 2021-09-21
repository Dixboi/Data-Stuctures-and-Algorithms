# Initialization of the node
class Node():
    
    def __init__(self, data = None):
        self.data = data
        self.next_node = None
        self.prev_node = None

class LinkedList():
    
    def __init__(self):
        self.head = Node() #head of the linked list
        
	# Adding a new element to the end of the list
    def add_last(self, data):
        new_node = Node(data)
        current_node = self.head
        
        while current_node.next_node != None:
            current_node.prev_node = current_node
            current_node = current_node.next_node
            
        current_node.next_node = new_node
        
    def add_first(self, data):
        new_node = Node(data)
        first_node = self.head.next_node
        
        self.head.next_node = new_node
        new_node.next_node = first_node
        first_node.prev_node = new_node
        new_node.prev_node = self.head
        
    #Iterate through the list
    def iterate(self):
        collection = []
        current_node = self.head
        
        while current_node.next_node != None:
            current_node = current_node.next_node
            collection.append(current_node.data)
            
        return collection
        
    #Removing or deleting the first match of the node
    def delete(self, data):
        if data not in self.iterate():
            print(data, "not in list")
        else:
            prev_node = self.head
            current_node = self.head.next_node
            
            while current_node.data != data:
                prev_node = current_node
                current_node = current_node.next_node
                
            prev_node.next_node = current_node.next_node
            current_node = current_node.next_node
            current_node.prev_node = prev_node
            
    # Search a specific data on a list
    def search(self, data):
        if data in self.iterate():
            return True
            
        return False
        
	# Displaying all elements of the list
    def display(self):
        current_node = self.head
        
        while current_node.next_node != None:
            current_node = current_node.next_node
            print(current_node.data, end = " ")
            
        print()
