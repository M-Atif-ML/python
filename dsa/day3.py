class hash_table:
	def __init__(self):
		self.MAX = 100
		self.arr = [[] for i in range(0,self.MAX)]
	def get_hash(self,key):
		h = 0
		for char in key:
			h += ord(char)
		return h % self.MAX

	def __setitem__(self,key,val):
		ind = self.get_hash(key)
		found = False

		for idx,element in enumerate(self.arr[ind]):
			if len(element) == 2 and element[0] == key:
				self.arr[ind][idx] = (key, val)
				found = True
				break
		if not found:
			self.arr[ind].append((key,val))

	def __getitem__(self,key):
		ind = self.get_hash(key)
		# print(ind)
		# print(key)
		for i in self.arr[ind]:
			if i[0] == key:
				return i[1]
		return "record not found"

	def __delitem__(self,key):
		ind = self.get_hash(key)
		for i,j in enumerate(self.arr[ind]):
			if j[0] == key:
				del self.arr[ind][i]
		

h = hash_table()
h["march 6"]=231
h["march 3"]=415
h["march 9"]=990
h["march 17"] = 123
h["march 6"]=31

# del h["march 9"] 
# print(h["march 2"])
# print(h.arr)/

del h["march 6"]
del h["march 17"]


# print(h[""])
# print(h["march 3"])
# print(h["march 9"])
# print(h["march 17"])
# print(h["march "])
