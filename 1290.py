# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        string = ''
        bit = 0
        value = 0
        while head is not None:
            # print(head.val)
            string = str(head.val) + string
            # bit += 1
            head = head.next
        for i in string:
            value += (2**bit)*int(i)
            bit += 1
        return value