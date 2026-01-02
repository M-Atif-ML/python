# linear probing

class hash_table:
	def __init__(self):
		self.MAX = 100
		self.arr = [None for i in range(0,self.MAX)]
	def get_hash(self,key):
		h = 0
		for char in key:
			h += ord(char)
		return h % self.MAX

	def __setitem__(self,key,val):  
		ind = self.get_hash(key)

		while self.arr[ind] != None:
			ind +=1 
			# print(self.arr[ind])

		self.arr[ind] = (key,val)


	def __getitem__(self,key):
		ind = self.get_hash(key)

		while self.arr[ind][0] != key:
			ind+=1
		return self.arr[ind][1]

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
h["march 6"] = -32

print(h["march 6"])

