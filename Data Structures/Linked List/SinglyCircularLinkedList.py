#Initialization of a node
class Node:

    def __init__(self, data = None):
        self.data = data
        self.next_node = None
    
class SinglyCircularLinkedList():
    
    def __init__(self):
        self.head = Node()
        self.tail = None
        
	#Add node on last part of the list
    def add(self, data):
        new_node = Node(data)
        current_node = self.head.next_node
        
        if current_node == None:
            self.tail = new_node
            self.head.next_node = self.tail
            self.tail.next_node = self.head
        else:
            new_node.next_node = current_node
            self.tail.next_node = new_node
            self.tail = new_node
            
	#Delete target node
    def delete(self, data):
        current_node = self.head.next_node
        
        if current_node.data == data:
            current_node = current_node.next_node
            self.tail.next_node = current_node
            self.head.next_node = current_node
        else:
            prev_node = current_node
            current_node = current_node.next_node
            
            while current_node.data != data:
                if current_node == self.head.next_node:
                    return
                prev_node = current_node
                current_node = current_node.next_node
            
            current_node = current_node.next_node
            prev_node.next_node = current_node
            
	#Display all nodes without stop
    def display(self):
        current_node = self.head
        
        while current_node.next_node != None:
            current_node = current_node.next_node
            print(current_node.data)
