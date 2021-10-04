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
                
            current_node = current_node.next_node
            prev_node.next_node = current_node
            
    # Search a specific data on a list
    def search(self, data):
        if data in self.iterate():
            return True
            
        return False
        
    # Reverse the list
    def reverse(self):
        prev_node = None
        current_node = self.head.next_node
        next_ = current_node.next_node
        
        while next_ != None:
            next_ = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_
            
        self.head.next_node = prev_node
        
	# Displaying all elements of the list
    def display(self):
        current_node = self.head
        
        while current_node.next_node != None:
            current_node = current_node.next_node
            print(current_node.data, end = " ")
            
        print()
