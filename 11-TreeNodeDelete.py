# Week 5 - 11) Based on the Python Code or the C++ Code Provided in class as a
#              starting point, implement the binary search tree node, delete
#              function.

class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert(self,n,x):
        #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x

    '''
Added remove function.
    '''
    def remove(self, node):
        '''Remove an item from a linked list data structure.'''
        # Sets the delete pointer to the first node
        deletePointer = self.head

        # Until the node is equal to the deletePointer.value
        while node != deletePointer.value:
            # Set the delete pointer to the next value
            deletePointer = deletePointer.next

        # If the previous pointer is equal to none.
        if deletePointer.prev != None:
            # Sets the previous deletePointer's next pointer to the next
            # pointer value.
            deletePointer.prev.next = deletePointer.next
        else:
            # Gets head value of the tree, and set to the next pointer.
            self.head = deletePointer.next

        # If the next value is none.
        if deletePointer.next != None:
            # Set the next previous deletePointer, to the previous
            # deletePointer.
            deletePointer.next.prev = deletePointer.prev
        else:
            # Set the tail of the deletePointer, previous.
            self.tail = deletePointer.prev
    
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print("List: ",",".join(values))
          
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.tail,Node(6))
    l.insert(l.tail,Node(8))
    l.insert(l.tail,Node(10))
    l.insert(l.tail,Node(13))
    l.display()
    l.remove(6)
    l.display()
