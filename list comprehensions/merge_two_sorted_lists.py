# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    currentNode1 = list1
    currentNode2 = list2
    mergedList = ListNode()
    if currentNode1 != None:
        mergedList.val = currentNode1.val
        currentNode1 = currentNode1.next
    elif currentNode2 != None:
        mergedList.val = currentNode2.val
        currentNode2 = currentNode2.next
    else:
        return
    
    mergedCurrent = mergedList
    
    while currentNode1 or currentNode2:
        if currentNode2 != None:
            mergedCurrent.next = ListNode(currentNode2.val)
            currentNode2 = currentNode2.next
            mergedCurrent = mergedCurrent.next

        if currentNode1 != None:
            mergedCurrent.next = ListNode(currentNode1.val)
            currentNode1 = currentNode1.next
            mergedCurrent = mergedCurrent.next

    return mergedList