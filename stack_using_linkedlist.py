class Node:
    def __init__(self,data):
        #creating instance variable
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    #checking stackisEmpty
    def stackisEmpty(self):
        return self.top==None
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode
    def pop(self):
        if(self.top==None):
            print("Stack Is Empty")
            return
        popped=self.top
        print(f"Pop Element is:{popped.data}")
        self.top=self.top.next
    def show(self):
        current=self.top
        print("Top",end="->")
        while(current!=None):
            print(current.data,end="->")
            current=current.next
        print("None")
    #top item in the stack
    def peek(self):
        if(stack.stackisEmpty(self)):
            return "Stack Is Empty!!"
        return f"Top of the Stack:{self.top.data}"
#mainmethod
if __name__=='__main__':
    s=stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.show()
    s.pop()
    s.show()
    s.pop()
    s.show()
    s.pop()
    s.show()
    print(s.peek())

    
    
