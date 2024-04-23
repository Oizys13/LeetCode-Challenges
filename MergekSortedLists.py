import heapq

class ListNode(object):
    def init(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Create a priority queue to store the nodes to be merged
        queue = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(queue, (node.val, i))
        
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        current = dummy
        
        while queue:
            # Extract the node with the smallest value from the queue
            val, i = heapq.heappop(queue)
            current.next = ListNode(val)
            current = current.next
            
            # Add the next node from the same list to the queue
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(queue, (lists[i].val, i))
        
        return dummy.next