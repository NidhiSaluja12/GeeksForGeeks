'''Example 1:

â€‹Input : arr[ ] = {1, 2, 3, 4}
Output : 21
Explanation:
Sum up an array from index 0 to 1 = 3
Sum up an array from index 2 to 3 = 7
Their multiplication is 21.â€‹â€‹

â€‹Example 2:

Input : arr[ ] = {1, 2}
Output :  2


Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function multiply() that takes an array (arr), sizeOfArray (n), and return the sum of the subarrays and then multiply both the subarrays. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).


Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ A[i] ≤ 100
'''


# User function Template for python3

def multiply(arr, n):
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    sum_left = sum(left)
    sum_right = sum(right)
    return sum_left * sum_right
    # Complete the function


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# } Driver Code Ends
