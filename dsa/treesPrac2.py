class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(2)
n2 = Node(3)
# n2.next=n1
n3 = Node(1)
# n3.next=n2

def add(prev,val):
    prev.next= val

add(n3,n2)
add(n2,n1)


for i in range(3):
    print(n3.data)
    n3 = n3.next

