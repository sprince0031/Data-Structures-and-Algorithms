class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head
    def insert(self, value):
        newNode = Node(value)
        newNode.setNextNode(self.head)
        self.head = newNode
        return "Value {} successfully inserted.".format(head.value)
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNextNode()
        return count
    def search(self, value):
        current = self.head
        found = False
        while current and found is False:
            if current.getValue() == value:
                found = True
            else:
                current = current.getNextNode()
        if current is None:
            raise ValueError("Data not found!")
        return found
    def delete(self, value):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getValue() == value:
                found = True
            else:
                previous = current
                current = current.getNextNode()
        if current is None:
            raise ValueError("Data not found!")
        if previous is None:
            self.head = current.getNextNode()
        else:
            previous.setNextNode(current.getNextNode())

class Node(object):
    def __init__(self, value = None, nextNode = None):
        self.value = value
        self.nextNode = nextNode
    def getValue(self):
        return self.value
    def getNextNode(self):
        return self.nextNode
    def setNextNode(self, newNode):
        self.nextNode = newNode

L = SinglyLinkedList
print(L.insert(int(input())))
print(L.insert(int(input())))
print(L.size())
print(L.search(int(input())))
print(L.delete(int(input())))