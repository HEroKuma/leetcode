# Implement the following operations of a queue using stacks.
#
#
# 	push(x) -- Push element x to the back of the queue.
# 	pop() -- Removes the element from in front of the queue.
# 	peek() -- Get the front element.
# 	empty() -- Return whether the queue is empty.
#
#
# Notes:
#
#
# 	You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# 	Depending on your language, the stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# 	You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
#
#
#  
# Example 1:
#
#
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
#
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1);
# myQueue.push(2);
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1
# myQueue.empty(); // return False
#
#
#  
# Constraints:
#
#
# 	1 <= x < 10
# 	At most 100 calls will be made to push, pop, peek, and empty.
#
#


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = list()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        ele = self.queue[0]
        del(self.queue[0])
        return ele
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if len(self.queue) != 0 else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
