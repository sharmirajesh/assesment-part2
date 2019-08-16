class node:
    def __init__(self,data):
        self.data=data
        self.nxt=None
class slinkedlist:
    def __init__(self):
        self.headval=None
    def atend(self,newdata):
        newnode=node(newdata)
        if self.headval is None:
            self.headval=newnode
            return
        last=self.headval
        
        while(last.nxt):
            last=last.nxt
        last.nxt=newnode
    def PrintList(self):
         printval=self.headval
         while printval is not None:
             print(printval.data,'==>',end='')
             printval=printval.nxt
         print("None")
    def delatend(self):
        prev=self.headval
        last=self.headval
        while(last.nxt):
            prev=last
            last=last.nxt
        prev.nxt=None    
obj=slinkedlist()
ch=0
while(ch!=4):
    print("1.Insert 2.Delete  3.Print  4.Exit")
    ch=int(input("Enter ur choice:"))
    if(ch==1):
        a=input()
        obj.atend(a)
        obj.PrintList()
    elif(ch==2):
        obj.delatend()
        obj.PrintList()
    elif(ch==3):
        obj.PrintList()
    else:
        break
