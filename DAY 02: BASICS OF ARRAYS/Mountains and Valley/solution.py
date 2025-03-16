class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
          
        else:
            self.tail.next = new_node
            self.tail = new_node

def user_logic(linked_list):
    # If the linked list has only one node, return 1
    if not linked_list.head or not linked_list.head.next:
        return 1

    current = linked_list.head
    increasing = None  # None means we haven't determined the pattern yet

    while current and current.next:
        if current.data == current.next.data:
            return 0  # No two consecutive elements should be equal
        
        if current.data < current.next.data:
            if increasing is False:  # Previous trend was decreasing, now increasing
                increasing = True
              
            elif increasing is None:
                increasing = True
              
            else:
                return 0  # Not alternating
              
        else:  # current.data > current.next.data
            if increasing is True:  # Previous trend was increasing, now decreasing
                increasing = False
              
            elif increasing is None:
                increasing = False
              
            else:
                return 0  # Not alternating
        
        current = current.next

    return 1

def main():
    import sys
    input = sys.stdin.read
  
    data = input().strip().split()
    n = int(data[0])
  
    values = list(map(int, data[1:]))
    ll = LinkedList()
  
    for value in values:
        ll.push(value)
      
    result = user_logic(ll)
    print(result)

if __name__ == "__main__":
    main()
