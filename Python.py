class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        
    
def getMiddle(head):
    slow = head
    fast = head
        
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
            
    return slow.data
    
    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
        
    print(getMiddle(head))
        
if __name__ == "__main__":
    main()