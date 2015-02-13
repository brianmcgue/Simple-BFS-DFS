from bfs import BFS
from dfs import DFS
from node import Node

root = Node(value=10)
n1 = Node(value=6)
n2 = Node(value=14)
n3 = Node(value=1)
n4 = Node(value=8)
root.set_left(n1)
root.set_right(n2)
n1.set_left(n3)
n1.set_right(n4)


print """
           10
      6         14
  1       8
"""


print "BFS(8):"
bfs = BFS(root)
bfs.find(8)

print "\nDFS(8):"
dfs = DFS(root)
dfs.find(8)

print "\nBFS(14):"
bfs = BFS(root)
bfs.find(14)

print "\nDFS(14):"
dfs = DFS(root)
dfs.find(14)

