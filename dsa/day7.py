class TreeNode:
	def __init__(self,data):
		self.data = data
		self.childern = []
		self.parent = None

	def addChild(self,child):
		child.parent = self
		self.childern.append(child)

	def print_tree(self):
		spaces = 3*self.get_level()*" "
		prefix = spaces + "|__" if self.parent else ""
		print(prefix+self.data)
		if self.childern: 
			for child in self.childern:
				child.print_tree()
	def get_level(self):
		p = self.parent
		level = 0
		while p:
			level+=1
			p = p.parent
		return level

def build_product_tree():
	root = TreeNode("Electronics")

	laptop = TreeNode("Laptop")
	laptop.addChild(TreeNode("Mac"))
	laptop.addChild(TreeNode("Surface"))
	laptop.addChild(TreeNode("Thinkpad"))

	cellphone = TreeNode("Cell Phone")
	cellphone.addChild(TreeNode("iphone"))
	cellphone.addChild(TreeNode("Google pixel"))
	cellphone.addChild(TreeNode("vivo"))

	tv = TreeNode("TV")
	tv.addChild(TreeNode("Samsung"))
	tv.addChild(TreeNode("LG"))

	root.addChild(laptop)
	root.addChild(cellphone)
	root.addChild(tv)
	return root

if __name__ == "__main__":
	

	root = build_product_tree()
	root.print_tree()
