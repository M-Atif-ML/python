class BinarySearchTreeNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self,data):
		if data == self.data:
			return 

		if data < self.data:
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BinarySearchTreeNode(data)			

		else:
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BinarySearchTreeNode(data)


	def search(self,val):
		if self.data == val :
			return True

		if val < self.data:
			if self.left:
				return self.left.search(val)
			else:
				 return False
		if val > self.data:
			if self.right:
				return self.right.search(val)
			else:
				 return False

	def in_order_traversal(self):
		elements = []

		# visit left tree
		if self.left:
			elements += self.left.in_order_traversal()

		elements.append(self.data)
		# visit right tree
		if self.right:
			elements+= self.right.in_order_traversal()

		return elements

	def find_min(self):
		if self.left == None:
			return self.data
		return self.left.find_min()

	def find_max(self):
		if self.right == None:
			return self.data
		return self.right.find_max()

	def find_sum(self):
	    total = self.data

	    if self.left:
	        total += self.left.find_sum()

	    if self.right:
	        total += self.right.find_sum()

	    return total

	def pre_order_traversal(self):
		elements = []

		elements.append(self.data)

		if self.left:
			elements += self.left.pre_order_traversal()
		if self.right:
			elements += self.right.pre_order_traversal()

		return elements


	def post_order_traversal(self):
		elements = []

		elements.append(self.data)

		if self.left:
			elements += self.left.pre_order_traversal()
		if self.right:
			elements += self.right.pre_order_traversal()

		return elements

	def delete(self,val):
		if val < self.data:
			if self.left:
				self.left=self.left.delete(val)
		elif val > self.data:
			if self.right:
				self.right=self.right.delete(val)
		else:
			if self.left is None and self.right is None:
				return None

			if self.left is None:
				return self.right
			if self.right is None:
				return self.left

			min_val = self.right.find_min()
			self.data = min_val
			self.right = self.right.delete(min_val)
		return self


def build_tree(elements):
	root = BinarySearchTreeNode(elements[0])

	for i in range(1,len(elements)):
		root.add_child(elements[i])
	return root

numbers = [17,4,1,20,9,23,18,34]
numbers_tree = build_tree(numbers)
# print(numbers_tree.in_order_traversal()) 
# print(numbers_tree.search(11)) 
# print(numbers_tree.find_min())
# print(numbers_tree.find_max())
# print(numbers_tree.find_sum())

print(numbers_tree.pre_order_traversal())
numbers_tree.delete(17)
numbers_tree.delete(34)
print(numbers_tree.pre_order_traversal())