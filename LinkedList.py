class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def addLast(self,data):
        if(self.head==None):
            newNode=Node(data) #creating Node
            self.head=newNode
            return newNode
        newNode=Node(data)
        current=self.head
        while(current.next!=None):
            current=current.next
        current.next=newNode
    def deleteLast(self):
        if(self.head==None):
            print("LL is Empty!!")
            return
        elif(self.head.next==None):
            self.head=None
            return 
        current=self.head
        while(current.next.next!=None):
            current=current.next
        current.next=None
    def display(self):
        current=self.head
        while(current!=None):
            print(current.data,end="->")
            current=current.next
        print("None")
if __name__ =='__main__':
    l=ll()
    l.addLast(10)
    l.addLast(20)
    l.display()
    l.deleteLast()
    l.display()
    l.deleteLast()
    l.display()

        
            
        
