from queue import Queue

class DFS(Queue):

	def __init__(self, root):
		super(self.__class__, self).__init__(root)

	def find(self, value):
		while self.queue:
			this_node = self.queue.pop()
			print this_node.value
			if this_node.value == value:
				return this_node

			if this_node.right is not None:
				self.queue.append(this_node.right)

			if this_node.left is not None:
				self.queue.append(this_node.left)

		return None
