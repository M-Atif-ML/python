from python_utils.singly_linkList import  LinkedList

l = LinkedList()
l.insert_values([1,2,3,4,9,12,13,14])

l.print()

def get_by_val(lArr, val):
    temp = lArr.head

    while temp:

        if temp.data == val:
            return temp
        temp = temp.next

    return None

def swap_by_vals(lArr,val1,val2):

    node1= get_by_val(lArr, val1)
    node2= get_by_val(lArr, val2)
    if node1 and node2:
        node1.data ,node2.data = node2.data,node1.data

def continuous_swap(lArr):

    temp = lArr.head
    while temp and temp.next:
        swap_by_vals(lArr, temp.data, temp.next.data)
        temp = temp.next.next



continuous_swap(l)
l.print()


