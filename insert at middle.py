class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class slinkedlist:
    def __init__(self):
        self.head=None
#function to add new node
    def inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("the mentioned node is absent")
            return
        newnode=node(newdata)
        newnode.next=middle_node.next
        middle_node.next=newnode
        
#print the linked list
    def listprint(self):
        temp=self.head
        while temp is not None:
            print(temp.data,"==>",end=' ')
            temp=temp.next
#create an object
list=slinkedlist()
#insert a data
list.head=node("mon")
e2=node("tue")
e3=node("wed")
#link the node
list.head.next=e2
e2.next=e3
#insert the middle value
list.inbetween(list.head.next,"thur")
list.listprint()
