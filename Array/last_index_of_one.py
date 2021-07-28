'''Given a string S consisting only '0's and '1's,  find the last index of the '1' present in it.



Example 1:

Input:
S = 00001
Output:
4
Explanation:
Last index of  1 in given string is 4.


Example 2:

Input:
0
Output:
-1
Explanation:
Since, 1 is not present, so output is -1.



Your Task:
You don't need to read input or print anything. Your task is to complete the function lastIndex() which takes the string S as inputs and returns the last index of '1'. If '1' is not present, return "-1" (without quotes).



Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)



Constraints:
1 <= |S| <= 106
S = {0,1}

 '''


# User function Template for python3

class Solution:
    def lastIndex(self, s):

        s.split()

        if '1' not in s:
            return -1

        for i in range(0, len(s))[::-1]:
            if s[i] == '1':
                return i

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while T > 0:
        s = input()
        ob = Solution()
        print(ob.lastIndex(s))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
