#Initialize queue
class Node():
    
    def __init__(self, data = None):
        self.data = data
        self.next_node = None
        self.prev_node = None

class NodeQueue():
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
    
	#add element to queue
    def enqueue(self, data):
        new_node = Node(data)
        #if queue is empty
        if self.head.next_node == self.tail and self.tail.prev_node == self.head:
            self.head.next_node = new_node
            self.tail.prev_node = new_node
            new_node.next_node = self.tail
            new_node.prev_node = self.head
        #if queue is not empty
        else:
            first_node = self.head.next_node
            new_node.prev_node = self.head
            new_node.next_node = first_node
            self.head.next_node = new_node
            first_node.prev_node = new_node
    
	#remove element from queue
    def dequeue(self):
        last_node = self.tail.prev_node
        new_last = last_node.prev_node
        self.tail.prev_node = new_last
        new_last.next_node = self.tail
    
	#display elements of queue
    def display(self):
        current_node = self.tail
        while current_node.prev_node != self.head:
            current_node = current_node.prev_node
            print(current_node.data)
