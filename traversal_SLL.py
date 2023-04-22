class Node:
    def __init__(self,data):
        # print('---------------------------------------------------------------------------------------------')

        self.data=data
        # print(self.data,'self.data in Node')
        self.refer=None

class SLL:
    def __init__(self):
        self.head=None
        # print(self.head,'self.head')
    
    def Traversal(self):
        if self.head is None:
            print(' wavvvv the SLL is empty')
        else:
            a=self.head
            # print(a,'aseffff')
            while a is not None:
                print(a.data,'a.data')
                a=a.refer
    
    # insertion at begining
    def in_beg(self,data):
        nb=Node(data)
        nb.refer=self.head
        self.head=nb



sll=SLL()
n1=Node(1)
n2=Node(2)
n1.refer=n2

n3=Node(3)
n2.refer=n3

n4=Node(4)
n3.refer=n4


n5=Node(5)
n4.refer=n5


sll.head=n1
sll.in_beg(100012)
sll.Traversal()


