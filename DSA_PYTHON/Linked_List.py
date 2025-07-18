
"""
Linked List :-
- A linked list is a type of linear data structure similar to arrays. 
    It stores data in non-contiguous memory locations.
- It is a collection of nodes that are linked with each other. A node contains 
    two things first is data and second is a link that connects it with another node.
- Contiguous vs. Non-Contiguous:
    Arrays require contiguous memory allocation, meaning their elements must be stored 
    in a single, unbroken block of memory. Linked lists, on the other hand, use non-contiguous 
    allocation, where each node can be placed in any available memory location. 
- Nodes and Pointers:
    Linked lists are composed of nodes, and each node contains data and a pointer (or reference) 
    to the next node in the sequence. This pointer mechanism is how the list maintains its 
    structure despite the non-contiguous memory layout. 
- Advantages of Non-Contiguous Allocation:
    Flexibility: Linked lists can easily grow or shrink as needed, as nodes can be added or 
    removed without affecting the overall memory layout significantly. 
    Efficient Insertion/Deletion: Inserting or deleting elements in a linked list is efficient 
    because it only involves updating pointers, unlike arrays where shifting elements might be 
    necessary. 
- Disadvantages of Non-Contiguous Allocation:
    Overhead: Pointers consume extra memory space, which can be a concern in resource-constrained 
    environments. 
    Cache Misses: Due to the scattered nature of nodes, accessing elements in a linked list can 
    be slower than accessing elements in an array (which benefits from spatial locality and cache 
    hits).
- Note : 
    When we need to do more write operation can go for Linked List and if need to do more 
    read operatons can go with array.
    Like arrays, it is also used to implement other data structures like stack, queue and deque. 

- Linked List:
    Data Structure: Non-contiguous
    Memory Allocation: Typically allocated one by one to individual elements
    Insertion/Deletion: Efficient
    Access: Sequential
- Array:
    Data Structure: Contiguous
    Memory Allocation: Typically allocated to the whole array
    Insertion/Deletion: Inefficient
    Access: Random
"""

# First create Node

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        #Empty LL = Head = None
        self.head = None
        #for counting number of nodes or len of LL
        self.n = 0 
    #for get length of LL
    def __len__(self):
        return self.n
    
    #For add item as a head
    def insert_head(self,value):
        #new node (head=None)
        new_node = Node(value)
        #create connection
        new_node.next = self.head
        #re-assign head
        self.head = new_node
        #count
        self.n = self.n + 1

    #For Print or traverse LL
    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result = result + str(current.data) + '->'            
            current = current.next
        return result[:-2]
    
    #append means add new value at end or tail
    def append(self,value):
        new_node = Node(value)
        #for handle empty node exception
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        current = self.head
        while current.next != None:
            current = current.next

        #reached at last node
        current.next = new_node
        self.n = self.n + 1

    #For inser item in between of LL
    def insert_after(self,after,value):
        new_node = Node(value)

        current = self.head
        while current != None:
            if current.data == after:
                break
            current = current.next

        #Case 1 : break means item found currnet != None
        if current != None:
            new_node.next = current.next
            current.next = new_node
            self.n = self.n + 1
        #Case 2 : did not break means run full loop but item not found current = None
        else:
            return 'item not found in LL'
        
    #For making to LL as empty
    def clear(self):
        self.head = None
        self.n = 0

    #For delete from head in LL
    def delete_head(self):
        if self.head == None:
            return 'Empty LL'
        self.head = self.head.next
        self.n = self.n - 1

    # pop is to delete from tail or last item from LL
    def pop(self):
        #handling if Empty LL
        if self.head == None:
            return 'Empty LL'
        
        current = self.head
        #check if LL is having 1 item only
        if current.next == None:
            #if 1 tem means it head only
            self.delete_head()
            return
        #check for more than 1 item in LL to delete from tail
        while current.next.next != None:
            current = current.next

        #current -> 2nd last node
        current.next = None
        self.n = self.n - 1

    #remove by value in LL
    def remove(self,value):
        #handling if Empty LL
        if self.head == None:
            return 'Empty LL'
        #if looking to delete head itself
        if self.head.data == value:
            return self.delete_head()
        
        current = self.head
        while current.next != None:
            if current.next.data == value:
                break
            current = current.next
            #if not found
            if current.next == None:
                return 'Not Found'
            #if data found
            else:
                current.next = current.next.next
                self.n = self.n - 1

    #search item by value in LL
    def search_value(self,item):
        current = self.head
        position = 0
        while current != None:
            if current.data == item:
                return position
            current = current.next
            position = position + 1
        return 'Item Not Found'
    
    #Search item by index in LL
    def __getitem__(self,index):
        current = self.head
        position = 0

        while current != None:
            if position == index:
                return current.data
            current = current.next
            position = position + 1
        return 'IndexError'


        
            



    



ll = LinkedList()
# print(ll)
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.append(55)
ll.insert_after(2,22)
#ll.clear()
#ll.delete_head()
#ll.pop()
ll.remove(2)
ll.remove(22)
print(ll.search_value(3))
print(ll.__getitem__(2))
#print(len(ll))
print(ll)
