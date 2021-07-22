'''Given a linked list of size N, your task is to complete the function isLengthEvenOrOdd() which contains head of the linked list and check whether the length of linked list is even or odd.

Input:
The input line contains T, denoting the number of testcases. Each testcase contains two lines. the first line contains N(size of the linked list). the second line contains N elements of the linked list separated by space.

Output:
For each testcase in new line, print "even"(without quotes) if the length is even else "odd"(without quotes) if the length is odd.

User Task:
Since this is a functional problem you don't have to worry about input, you just have to  complete the function isLengthEvenOrOdd() which takes head of the linked list as input parameter and returns 0 if the length of the linked list is even otherwise returns 1.

Constraints:
1 <= T <= 100
1 <= N <= 103
1 <= A[i] <= 103

Example:
Input:
2
3
9 4 3
6
12 52 10 47 95 0

Output:
Odd
Even

Explanation:
Testcase 1: The length of linked list is 3 which is odd.
Testcase 2: The length of linked list is 6 which is even.'''


# your task is to complete this function
# function should return true/1 if length is even
# else return false/0
def isLengthEvenOrOdd(head):
    count = 0
    result = "Odd"
    temp = head
    while temp is not None:
        temp = temp.next
        count += 1
    if count % 2 == 0:
        return "Even"

    # Code here


# {
#  Driver Code Starts
# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        if (isLengthEvenOrOdd(head)):
            print('Even')
        else:
            print('Odd')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
