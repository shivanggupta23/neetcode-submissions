class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if(i=="(" or i=="[" or i=="{"):
                stack.append(i)

            else:
                if len(stack)==0:
                    return False
                x=stack[-1]
                stack.pop()
                if i==")" and x!="(":
                    return False
                if i=="]" and x!="[":
                    return False
                if i=="}" and x!="{":
                    return False       
        return len(stack)==0