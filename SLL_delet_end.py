class Node:
    def __init__(self,data):
        # print('---------------------------------------------------------------------------------------------')

        self.data=data
        # print(self.data,'self.data in Node')
        self.refer=None

class SLL:
    def __init__(self):
        self.head=None

    def Traversal(self):
        if self.head is None:
            print(' wavvvv the SLL is empty')
        else:
            a=self.head
            # print(a,'aseffff')
            while a is not None:
                print(a.data,'a.data')
                a=a.refer
    
   

    def delet_end(self):
        print()
        pre=self.head
        a=self.head.refer
        
        while a.refer is not None:
            a=a.refer
            pre=pre.refer
        pre.refer=None

   


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
sll.Traversal()

sll.delet_end()

sll.Traversal()