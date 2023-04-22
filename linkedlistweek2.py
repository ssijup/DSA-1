class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None
        # print('node')


class SinglyLinkedList:
    def __init__(self):
        self.head=None
        # print('op')

    def append(self,value):
        new_node=Node(value)
        a=self.head
        if self.head is None:
            self.head=new_node
            
            # print(new_node.data)

        else:
            while a.next is not None:
                a=a.next
            a.next=new_node
            new_node.pre=a
            print(a.data,end=" ")
    
    def singlylinkedyravesal(self):
        a=self.head
        while a is not None:
           print(a.data)
           a=a.next
           
    def backwardtraversal(self):
        a=self.head
        if a is None:
            print("the linked list is empty")
        else:
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=" ")
                a=a.pre
                


sll_obj=SinglyLinkedList()
sll_obj.append(10)
sll_obj.append(11)
sll_obj.append(12)
sll_obj.append(13)
sll_obj.append(14)
sll_obj.append(15)
sll_obj.singlylinkedyravesal()
sll_obj.backwardtraversal()

