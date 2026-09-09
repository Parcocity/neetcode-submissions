class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1)
        self.num = {}
        self.address ={}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.num:
            return -1
        value = self.num[key]
        curr = self.address[key]
        prev = curr.prev
        prev.next = curr.next
        curr.next.prev = prev
        
        tail = self.head.prev
        tail.next = curr
        curr.prev = tail
        curr.next = self.head
        self.head.prev = curr

        return value
        
    def put(self, key: int, value: int) -> None:
        self.num[key] = value
        if key in self.address:
            curr = self.address[key]
            prev = curr.prev
            prev.next = curr.next
            curr.next.prev = prev
            
            tail = self.head.prev
            if tail:
                tail.next = curr
                curr.prev = tail
            else:
                self.head.next = curr
                curr.prev = self.head

            curr.next = self.head
            self.head.prev = curr

        else:
            curr = Node(key)
            self.address[key] = curr

            tail = self.head.prev
            if tail:
                tail.next = curr
                curr.prev = tail
            else:
                self.head.next = curr
                curr.prev = self.head

            curr.next = self.head
            self.head.prev = curr

        if len(self.num) > self.capacity:
            old = self.head.next
            self.head.next = old.next
            old.next.prev = self.head
            old.next = None
            old.prev = None
            self.num.pop(old.val)
            self.address.pop(old.val)
        
class Node:
    def __init__(self, key=0):
        self.val = key
        self.next = None
        self.prev = None


