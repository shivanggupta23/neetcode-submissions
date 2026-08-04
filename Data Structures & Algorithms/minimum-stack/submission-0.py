class MinStack:
    stack1=[]
    stack2=[]
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, val: int) -> None:
        self.stack1.append(val)
        if(len(self.stack2)==0):
            self.stack2.append(val)
        else:
            if val<=self.stack2[-1]:
                self.stack2.append(val)    

    def pop(self) -> None:
        x=self.stack1[-1]
        self.stack1.pop()
        if(len(self.stack2)!=0):
            if(self.stack2[-1]==x):
                self.stack2.pop()
        

    def top(self) -> int:
        return self.stack1[-1]  

    def getMin(self) -> int:
        return self.stack2[-1]
