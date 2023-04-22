class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class DLL:
    def __init__(self):
        self.head=None

    
    
    def add_node(self,value):
        new_node=Node(value)
        a=self.head
        if self.head is None:
            self.head=new_node
        else:
            while a.next is not None:
                a=a.next 
            a.next=new_node
            new_node.prev=a
            print(new_node.data,'op')

    
    def dll_trevesal(self):
        print()
        a=self.head
        if a is None:
            print('Double linked list is empty')
        else:
            a=self.head
            while a is not None:
               
                print(a.data,end="  ")
                a=a.next

    def dll_backward_traversal(self):
        print()
        a=self.head
        if a is None:
            print('Double linked list is empty')
        else:
            a=self.head
            prev=self.head
            while a.next is not None:   
                # print(a.data)
             
                a=a.next
                         
            while a is not None:
                print(a.data,end="  ")
                a=a.prev
                

    # def dll_insert_at_beg(self,data):
    #     print()
    #     nb=Node(data)
    #     a=self.head
    #     self.head=nb
    #     nb.next=a

    #     a.prev=nb
     

    # def dll_insert_at_end(self,data):
    #     print()
    #     end=Node(data)
    #     a=self.head.next
    #     prev=self.head
    #     while a.next is not None:
    #         a=a.next
    #     a.next=end
    #     end.prev=a
        

    # def dll_insert_at_specific_pooos(self,data,pos):
    #     spe_node=Node(data)
    #     # af=self.head.next
    #     a=self.head
    #     for i in range(1,pos-1):
    #         a=a.next

        
    #     spe_node.prev=a
    #     spe_node.next=a.next
    #     a.next.prev=spe_node
    #     a.next=spe_node
       
            # af=af.next
        # a.next=spe_node
        # spe_node.next=af
        # # af.prev=spe_node
        # spe_node.prev=a

        

    # def dll_del_at_begg(self):
    #     a=self.head
    #     af=a.next

    #     a.next=None
    #     self.head=af
    #     af.prev=None


    # def dll_del_at_end(self):
    #     a=self.head.next
    #     prev=self.head
    #     while a.next is not None:
    #         a=a.next
    #         prev=prev.next
    #     prev.next=None
    #     a.prev=None
        
    # def dll_del__at_specific_pos(self,pos):
    #     a=self.head.next
    #     prev=self.head
    #     for i in range(1,pos-1):
    #         a=a.next
    #         prev=prev.next

    #     ab=a.next
    #     a.next=None
    #     a.prev=None

    #     prev.next=ab
    #     ab.prev=prev


    # def add_TwoNode(self,data1,data2):
    #     a=self.head
    #     main=self.head.next
    #     while main.next is not None:
    #         main=main.next
    #         a=a.next
    #         new1=Node(data1)
    #         new2=Node(data2)
    #         if main.data == 77:
    #             a.next=new1
    #             new1.next=new2
    #             new2.prev=new1
    #             new2.next=main
    #             main.prev=new2
    #             new1.prev=a
        

        

dll=DLL()
# n1=Node(1)
# dll.head=n1


# n2=Node(2)
# n1.next=n2
# n2.prev=n1

# n3=Node(3)
# n2.next=n3
# n3.prev=n2

# n4=Node(4)
# n3.next=n4
# n4.prev=n3

# n5=Node(5)
# n4.next=n5
# n5.prev=n4


dll.dll_trevesal()

dll.add_node(11)
dll.add_node(22)
dll.add_node(33)
dll.add_node(44)
dll.add_node(55)
dll.add_node(66)
dll.add_node(77)
dll.add_node(88)
dll.add_node(99)

# dll.dll_trevesal()
# dll.dll_insert_at_end(99)
# dll.dll_insert_at_beg(10)
# dll.dll_trevesal()
# dll.add_TwoNode(100,99999)
dll.dll_trevesal()

# dll.dll_del__at_specific_pos(3)
# dll.dll_del_at_end()
# dll.dll_del_at_begg()
# dll.dll_insert_at_specific_pooos(999,3)
# dll.dll_trevesal()
dll.dll_backward_traversal()
