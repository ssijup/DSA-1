class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.main=None

    def insert_begining(self):
        if self.main is None:
            print("The list is empty")
        else:
            a=self.main
            while a is not None:
                print(a.data)
                a= a.next

n1=Node(1)

sll=SLL()

n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)



nb=Node(100)
sll.main=nb
nb.next=n1
# sll.main=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5


sll.insert_begining()
