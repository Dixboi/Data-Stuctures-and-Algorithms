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
        
	# Returning the length of the list
    def length(self):
        count = 0 
        current_node = self.head
        
        while current_node.next_node != None:
            current_node = current_node.next_node
            count += 1
            
        return count
        
	# Getting the data on a specific index
    def getDataOn(self, index):
        if index >= self.length() or index < 0:
            return "None"
        
        current_index = 0
        current_node = self.head
        
        while True:
            current_node = current_node.next_node
            if current_index == index:
                return current_node.data
                
            current_index += 1
            
	# Removing data on a specific index
    def removeDataOn(self, index):
        if index >= self.length() or index < 0:
            return None
            
        current_index = 0
        current_node = self.head
        
        while True:
            prev_node = current_node
            current_node = current_node.next_node
            if current_index == index:
                prev_node.next_node = current_node.next_node
                break
                
            current_index += 1
        
	# Finding the index of a specific data
    def indexOf(self, data):
        current_index = 0
        current_node = self.head

        while current_node.next_node != None:
            current_node = current_node.next_node
            if current_node.data == data:
                return current_index
                
            current_index += 1
            
        return None
        
	# Displaying all elements of the list
    def display(self):
        current_node = self.head
        
        while current_node.next_node != None:
            current_node = current_node.next_node
            print(current_node.data, end = " ")
            
        print()
