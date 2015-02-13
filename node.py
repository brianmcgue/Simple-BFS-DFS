class Node:

	def __init__(self, value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None

	def set_left(self, new_left):
		new_left.parent = self
		self.left = new_left

	def set_right(self, new_right):
		new_right.parent = self
		self.right = new_right
