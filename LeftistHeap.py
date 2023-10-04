class LeftistNode:
    def __init__(self, element, lt=None, rt=None, dist=0):
        self.element = element
        self.left = lt
        self.right = rt
        self.dist = dist
 
class LeftistHeap:
    def __init__(self):
        self.root = None
 
    # Merge two heaps preserving leftist property
    def merge(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.element < h2.element:
            return self.merge1(h1, h2)
        else:
            return self.merge1(h2, h1)
 
    # Merge h2 into h1, assumes h1's root element is smaller
    def merge1(self, h1, h2):
        if not h1.left:
            h1.left = h2
        else:
            h1.right = self.merge(h1.right, h2)
            if h1.left.dist < h1.right.dist:
                self.swap_children(h1)
            h1.dist = h1.right.dist + 1
        return h1
 
    # Swap children of a node
    def swap_children(self, t):
        t.left, t.right = t.right, t.left
 
    # Insert an element into the heap
    def insert(self, x):
        self.root = self.merge(LeftistNode(x), self.root)
 
    # Find the minimum element in the heap
    def find_min(self):
        if self.root:
            return self.root.element
        else:
            raise Exception("Heap is empty")
 
    # Delete the minimum element from the heap
    def delete_min(self):
        if self.root:
            old_root = self.root
            self.root = self.merge(self.root.left, self.root.right)
            return old_root.element
        else:
            raise Exception("Heap is empty")
 
    # Check if the heap is empty
    def is_empty(self):
        return self.root is None
 
    # Make the heap logically empty
    def make_empty(self):
        self.root = None
 
def main():
    h = LeftistHeap()
    h1 = LeftistHeap()
    h2 = LeftistHeap()
    arr = [1, 5, 7, 10, 15]
    arr1 = [22, 75]
 
    # Insert elements into h and h1
    for item in arr:
        h.insert(item)
 
    for item in arr1:
        h1.insert(item)
 
    # Delete and print minimum elements from h and h1
    x = h.delete_min()
    print(x)
 
    x = h1.delete_min()
    print(x)
 
    # Merge h and h1 into h2
    h2.root = h.merge(h.root, h1.root)
 
    # Delete and print minimum element from h2
    x = h2.delete_min()
    print(x)
 
if __name__ == "__main__":
    main()
