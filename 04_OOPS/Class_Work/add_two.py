class Addition:
	def set(self,a,b):
		self.a = a
		self.b = b
	def sum(self):
		self.c = self.a+self.b
	def display(self):
		return self.c

a = Addition()
a.set(10,20)
a.sum()
print(a.display())



'''
def set(self,a,b):
	self.a = a
	self.b = b

def add(self):
	print("Add is called")
	c = self.a + self.b
	return c
'''