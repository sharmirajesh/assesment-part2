class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class slinkedlist:
    def __init__(self):
        self.head=None
    def atbeginning(self,data_in):
        newnode=node(data_in)
        newnode.next=self.head
        self.head=newnode
    def removenode(self,removekey):
        headval=self.head
        if(headval is not None):
            if(headval.data==removekey):
                print("deltion at head")
                self.head=headval.next
                return
        else:
            print("the list is empty")
            return
        while(headval is not None):
            if headval.data==removekey:
                break
            prev=headval
            headval=headval.next
        else:
            print("the key is not available")
        if(headval==None):
            return
        prev.next=headval.next
        headval=None
    def llistprint(self):def __init__(self,data):
        self.data=data
        self.next=None
        printval=self.head
        while(printval):
            print(printval.data)
            printval=printval.next
llist=slinkedlist()
llist.removenode("tue")


llist.atbeginning("mon")
llist.atbeginning("tue")
llist.atbeginning("wed")
llist.atbeginning("thu")
llist.llistprint()
print("after removal of fri")
llist.removenode("fri")
llist.llistprint()

#llist.llistprint()
