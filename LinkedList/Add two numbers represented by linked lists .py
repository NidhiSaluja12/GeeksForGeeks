"""
Add two numbers represented by linked lists
Easy Accuracy: 30.12% Submissions: 100k+ Points: 2
Given two numbers represented by two linked lists of size N and M. The task is to return a sum list.

The sum list is a linked list representation of the addition of two input numbers from the last.

Example 1:

Input:
N = 2
valueN[] = {4,5}
M = 3
valueM[] = {3,4,5}
Output: 3 9 0
Explanation: For the given two linked
list (4 5) and (3 4 5), after adding
the two linked list resultant linked
list will be (3 9 0).
Example 2:

Input:
N = 2
valueN[] = {6,3}
M = 1
valueM[] = {7}
Output: 7 0
Explanation: For the given two linked
list (6 3) and (7), after adding the
two linked list resultant linked list
will be (7 0).
Your Task:
The task is to complete the function addTwoLists() which has node reference of both the linked lists and returns the head of the sum list.

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(Max(N,M)) for the resultant list.

Constraints:
1 <= N, M <= 5000


"""

# User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):


# code here
# return head of sum list

# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class
#User function Template for python3

''' Node for linked list:
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def convert_ll_to_arr(self, head):
        arr = []
        temp = head
        while temp is not None:
            arr.append(temp.data)
            temp = temp.next
        return arr
   
   
    def convert_arr_to_ll(self, arr):
        head = Node(arr[0])
        node = head
        for i in arr[1:]:
            node.next = Node(i)
            node = node.next
        return head
   
   
    def add_arrays(self, first, second):
        sum_arr = []
       
        S = 0
        carry = 0
       
        i = len(first) - 1
        j = len(second) - 1
       
        while i>=0 or j>=0:
            f_val = first[i] if i >= 0 else 0
            s_val = second[j] if j >= 0 else 0
           
            S = f_val + s_val + carry
            sum_arr.append(S % 10)
            carry = S // 10
           
            i -= 1
            j -= 1
       
        if carry:
            sum_arr.append(carry)
       
        return sum_arr[::-1]
   
   
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        sum_list = None
       
        # Conversion of linked list to array
        first_arr = self.convert_ll_to_arr(first)
        second_arr = self.convert_ll_to_arr(second)
       
        # Addition of two arrays
        sum_arr = self.add_arrays(first_arr, second_arr)
       
        # Conversion of array to linked list
        sum_list = self.convert_arr_to_ll(sum_arr)
       
        return sum_list
    
        
        # code here
        # return head of sum list

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
