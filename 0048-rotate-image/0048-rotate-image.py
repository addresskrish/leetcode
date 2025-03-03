class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r=0,len(matrix)-1
        while(l<r):
            for i in range(r-l):
                a,b,c,d=[l,l+i],[l+i,r],[r,r-i],[r-i,l]
                matrix[a[0]][a[1]],matrix[b[0]][b[1]],matrix[c[0]][c[1]],matrix[d[0]][d[1]]=matrix[d[0]][d[1]],matrix[a[0]][a[1]],matrix[b[0]][b[1]],matrix[c[0]][c[1]]
            l,r=l+1,r-1
        return