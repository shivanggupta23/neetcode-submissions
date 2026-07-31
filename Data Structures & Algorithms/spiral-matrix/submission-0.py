class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        colbeg=0
        colend=len(matrix[0])-1
        rowbeg=0
        rowend=len(matrix)-1
        while colbeg<=colend and rowbeg<=rowend:
            for j in range(colbeg,colend+1):
                ans.append(matrix[rowbeg][j])
            rowbeg+=1

            for i in range(rowbeg,rowend+1):
                ans.append(matrix[i][colend])
            colend-=1

            if rowbeg<=rowend:
                for j in range(colend,colbeg-1,-1):
                    ans.append(matrix[rowend][j])
                rowend-=1

            if  colbeg<=colend:
                for i in range(rowend,rowbeg-1,-1):
                    ans.append(matrix[i][colbeg])
                colbeg+=1

        return ans   