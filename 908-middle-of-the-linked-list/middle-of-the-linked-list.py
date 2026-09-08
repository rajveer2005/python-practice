class Solution(object):
    def middleNode(self, head):
        temp = head
        n = 0

        # Count nodes
        while temp is not None:
            n += 1
            temp = temp.next

        # Start again from head
        temp = head

        # Move to middle
        for i in range(n // 2):
            temp = temp.next

        return temp