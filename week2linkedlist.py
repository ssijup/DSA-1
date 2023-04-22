class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def addNode(self,data):
        newNode=Node(data)
        a=self.head
        if a is None:
            self.head=newNode
        else:
            while a.next is not None:
                a=a.next
            a.next=newNode

    def forwardTraverse(self):
        curr=self.head
        while curr is not None:
            print(curr.data,end="  ")
            curr=curr.next

    def addnodeatBegging(self,data):
        nodebeg=Node(data)
        curr=self.head
        self.head=nodebeg
        nodebeg.next=curr


obj=Linkedlist()
obj.addNode(10)
obj.addNode(11)
obj.addNode(12)
obj.addNode(13)
obj.addNode(14)
obj.addNode(15)
obj.forwardTraverse()
obj.addnodeatBegging(999)
obj.forwardTraverse()
