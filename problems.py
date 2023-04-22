class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None


    def print_value(self):
        a=self.head
        while a.next is not None:
            a=a.next
            print(a.data)
            if a.data == 30:
                print('Data found :',a.data)

            else:
                # print('not found')
                pass

sll=SLL()      
n1=Node(1)
sll.head=n1

n2=Node(30)
n1.next=n2

n3=Node(3)
n2.next=n3

n4=Node(4)
n3.next=n4

n5=Node(5)
n4.next=n5


sll.print_value()