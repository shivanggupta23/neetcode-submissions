class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"

        s1=num1[::-1]
        s2=num2[::-1]
        res=[0]*(len(s1)+len(s2))
        for i in range(len(s1)):
            carry=0
            start=i
            for j in range(len(s2)):
                n1=ord(s1[i])-ord('0')
                n2=ord(s2[j])-ord('0')
                total=n1*n2+carry+res[start]
                res[start]=total%10
                carry=total//10

                start+=1
            if carry!=0:
                res[start]+=carry

        i=len(res)-1
        while i>0 and res[i]==0:
            i-=1

        ans=""    
        while i>=0:
            ans+=str(res[i])
            i-=1
        return ans                   

        