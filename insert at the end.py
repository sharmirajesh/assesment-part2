class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class slinkedlist:
    def __init__(self):
        self.head=None
#function to add newnode
    def atend(self,newdata):
        newnode=node(newdata)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
  #use to check it is null or not
        while(last.next):
            last=last.next
        last.next=newnode
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
#insert the end value
list.atend("thur")
list.listprint()
