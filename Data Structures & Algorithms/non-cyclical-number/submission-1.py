class Solution:
    def isHappy(self, n: int) -> bool:
        list=[]
        while(True):
            sum=0
            while(n!=0):
                x=n%10
                sum=sum+x**2
                n=n//10
            if sum==1:
                return True
            if sum in list:
                return False    
            list.append(sum)
            n=sum
        return True    

