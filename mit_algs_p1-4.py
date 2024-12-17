def reorder_students(L):
    '''Input: L | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
    - any additional linked list nodes
    - any other non-constant-sized data structures'''
    #Divide by half,take 2nd half and reverse it
    slow = L.head
    fast = L.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    current = slow
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward
    
    first_half_tail = L.head
    while first_half_tail.next != slow:
        first_half_tail = first_half_tail.next
    
    first_half_tail.next = prev  # Connect first half to the reversed second half

'''
Solution:
def reorder_students(L):
    n = len(L) // 2 # find the n-th node
    a = L.head
    for _ in range(n - 1):
        a = a.next
    b = a.next # relink next pointers of last half
    x_p, x, x_p = a, b
    for _ in range(n):
        x_n = x.next
        x.next = x_p
        x_p, x = x, x_n
    c = x_p
    a.next = c # relink front and back of last half
    b.next = None
    return
'''

