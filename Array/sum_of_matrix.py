'''Given a non null integer matrix Grid of dimensions NxM.Calculate the sum of its elements.

Example 1:

Input:
N=2,M=3
Grid=
[[1,0,1],
[-8,9,-2]]
Output:
1
Explanation:
The sum of all elements of the matrix is
(1+0+1-8+9-2)=1.
Example 2:

Input:
N=3,M=5
Grid=
[[1,0,1,0,1],
[0,1,0,1,0],
[-1,-1,-1,-1,-1]]
Output:
0
Explanation:
The sum of all elements of the matrix are
(1+0+1+0+1+0+1+0+1+0-1-1-1-1-1)=0.


Your Task:
You don't need to read input or print anything.Your task is to complete the function sumOfMatrix() which takes two integers N ,M and a 2D array Grid as input parameters and returns the sum of all the elements of the Grid.


Expected Time Complexity:O(N*M)
Expected Auxillary Space:O(1)


Constraints:
1<=N,M<=1000
-1000<=Grid[i][j]<=1000
'''

#User function Template for python3

class Solution:
    def sumOfMatrix(self,N,M,Grid):
        sum1 = 0
        for i in range (N):
            for j in range(M):
                sum1+=Grid[i][j]
        return sum1
        #code here

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(' '))
        Grid = [[0 for i in range(M)] for j in range(N)]
        for i in range(N):
            s=list(map(int,input().strip().split(' ')))
            for j in range(M):
                Grid[i][j]=s[j]
        ob=Solution()
        print(ob.sumOfMatrix(N,M,Grid))
# } Driver Code Ends
