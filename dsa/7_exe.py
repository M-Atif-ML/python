# class TreeNode:
# 	def __init__(self,name,occupation):
# 		self.name = name
# 		self.occupation = occupation 
# 		self.childern = []
# 		self.parent = None

# 	def addChild(self,child):
# 		child.parent = self
# 		self.childern.append(child)

# 	def print_tree(self,form = "normal"):
# 		spaces = 3*self.get_level()*" "
# 		prefix = spaces + "|__" if self.parent else ""


# 		if(form == "normal"):
# 			print(prefix+f"{self.name}({self.occupation}) ")
# 		elif(form == "names"):
# 			print(prefix+f"{self.name}")
# 		elif(form == "occupation"):
# 			print(prefix+f"{self.occupation}")
# 		else:
# 			print("Invalid Format(Error)")
# 			return



# 		if self.childern: 
# 			for child in self.childern:
# 				child.print_tree(form)


# 	def get_level(self):
# 		p = self.parent
# 		level = 0
# 		while p:
# 			level+=1
# 			p = p.parent
# 		return level

# def build_product_tree():
# 	CEO = TreeNode("Atif khan","CEO")

# 	CTO = TreeNode("Chinmay","CTO")

# 	IH = TreeNode("John","Infrastructure Head")
# 	IH.addChild(TreeNode("Dhaval","Cloud Manager"))
# 	IH.addChild(TreeNode("Abhijit","App Manager"))

# 	AH = TreeNode("Amir","Application head")

# 	HR = TreeNode("Gels","HR head")
# 	HR.addChild(TreeNode("Peter","RM"))
# 	HR.addChild(TreeNode("Waqas","Policy Manager"))

# 	CTO.addChild(IH)
# 	CTO.addChild(AH)

# 	CEO.addChild(CTO)
# 	CEO.addChild(HR)

# 	return CEO

# if __name__ == "__main__":
	

# 	root = build_product_tree()
# 	root.print_tree(form = "normal")


# ==========================================================================

class TreeNode:
	def __init__(self,name):
		self.name = name

		self.childern = []
		self.parent = None

	def addChild(self,child):
		child.parent = self
		self.childern.append(child)

	def print_tree(self,level):
		spaces = 3*self.get_level()*" "
		prefix = spaces + "|__" if self.parent else ""

		if self.get_level() <= level :
			print(prefix+f"{self.name}")

		if self.childern: 
			for child in self.childern:
				child.print_tree(level)


	def get_level(self):
		p = self.parent
		level = 0
		while p:
			level+=1
			p = p.parent
		return level

def build_product_tree():
	root = TreeNode("Global")

	pakistan = TreeNode("Pakistan")

	kpk = TreeNode("KPK")
	kpk.addChild(TreeNode("Peshawar"))
	kpk.addChild(TreeNode("Swat"))

	punjab = TreeNode("Punjab")
	punjab.addChild(TreeNode("Lahore"))
	punjab.addChild(TreeNode("Multan"))

	usa = TreeNode("USA")

	newJersey = TreeNode("New Jersey")
	newJersey.addChild(TreeNode("Princeton"))
	newJersey.addChild(TreeNode("Trenton"))

	cal = TreeNode("California")
	cal.addChild(TreeNode("Los Angeles"))
	cal.addChild(TreeNode("San Francisco"))
	cal.addChild(TreeNode("Palo Alto"))

	usa.addChild(cal)
	usa.addChild(newJersey)
	pakistan.addChild(kpk)
	pakistan.addChild(punjab)
	root.addChild(pakistan)
	root.addChild(usa)

	return root


if __name__ == "__main__":
	

	root = build_product_tree()
	root.print_tree(2)

