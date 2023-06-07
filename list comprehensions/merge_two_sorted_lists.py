# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    currentNode1 = list1
    currentNode2 = list2
    mergedList = ListNode()
    mergedCurrent = mergedList
    
    while currentNode1 or currentNode2:
        if currentNode1 != None and currentNode2 != None:
            is1smaller = currentNode1.val < currentNode2.val
            mergedCurrent.next = ListNode(currentNode1.val if is1smaller else currentNode2.val)
            mergedCurrent = mergedCurrent.next
            if is1smaller:
                currentNode1 = currentNode1.next
            else:
                currentNode2 = currentNode2.next

        elif currentNode2 != None:
            mergedCurrent.next = ListNode(currentNode2.val)
            currentNode2 = currentNode2.next
            mergedCurrent = mergedCurrent.next

        elif currentNode1 != None:
            mergedCurrent.next = ListNode(currentNode1.val)
            currentNode1 = currentNode1.next
            mergedCurrent = mergedCurrent.next

    return mergedList.next



testList = ListNode(1)
testList.next = ListNode(2)
testList.next.next = ListNode(4)

testList2 = ListNode(1)
testList2.next = ListNode(3)
testList2.next.next = ListNode(4)

solution = mergeTwoLists(testList, testList2)
print('done')