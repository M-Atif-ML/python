""" doubly linklist """

class Node:
	def __init__(self,data = None,next = None,prev = None):
		self.data = data
		self.next = next
		self.prev = prev
class D_linkList:
	def __init__(self):
		self.head = None
		self.tail = None
	def insert_at_begining(self,data):
		node = Node(data,self.head)

		if self.head is None:
			self.head = node
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node 


	def print_forward(self):

		if self.head is None:
			print("Linked list is empty")
			return -1
		itr = self.head 
		listr = ""
		while itr:
			listr += str(itr.data) + "--->"
			itr= itr.next
		print(listr)

	def get_size(self):
		itr = self.head
		size= 0
		while itr:
			itr= itr.next
			size +=1
		return size
	def get_last_element(self):

		itr = self.head 
		for i in range(0,self.get_size()-1):
			itr = itr.next

		return itr
	def print_backwords(self):
		itr = self.get_last_element()
		istr = ""
		while itr:
			istr += f"{itr.data}--->"
			itr = itr.prev
		print(istr)


l = D_linkList()
l.insert_at_begining(1)
l.insert_at_begining(0)
l.insert_at_begining(0)
l.insert_at_begining(1)
# print(l.get_last_element())
l.print_backwords()
l.print_forward()