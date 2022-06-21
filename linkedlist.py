class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        if self.next == None:
            return '%s' % (self.data)
        else:
            return '%s, %s' % (self.data, self.next)

    def toString(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.next = None

    def __repr__(self):
        return '[' + str(self.head) + ']'

    def append(self, data):          
        new = Node(data)
        if self.head == None:
            self.head = new
            self.next = new
            self.last = new
        else:
            self.last.next = new
            self.last = new

    def getNextNode(self):
        if self.head == None:
            #print('-1')
            self.head
        elif self.next == None:
            #print('-2')
            node = self.head
            self.next = node.next
            return node.data
        else:
            #print('-3')
            node = self.next
            self.next = node.next
            return node.data
    
    def getCount(self,node='empty'):
        if node == 'empty':
            node = self.head
        if (not node): # Base case
            return 0
        else:
            return 1 + self.getCount(node.next)
