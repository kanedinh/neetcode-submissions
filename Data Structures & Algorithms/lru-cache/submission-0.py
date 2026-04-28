# Define Double Linked List
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

# Right: Most recently used
# Left: Least recently used

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # HashMap
        self.cache = {}
        # Dummy Node
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # Remove node from the list
    def remove(self, node: Optional[Node]) -> None:
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    # Insert key:value to the right
    def insert(self, node: Optional[Node]) -> None:
        prevNode = self.right.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.right
        self.right.prev = node
        
    # Get value of the key and move to the right (most recently used)
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    
    # Put the key:value to right of the list
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)
        
        if len(self.cache) > self.cap:
            lruNode = self.left.next
            self.remove(lruNode)
            del self.cache[lruNode.key]