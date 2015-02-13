from node import Node

class Queue(object):
	def __init__(self, root):
		if not isinstance(root, Node):
			print "Must supply root node"
			return

		self.queue = [root]
