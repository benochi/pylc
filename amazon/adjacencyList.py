class GraphNode:
  def __init__(self,val):
    self.val = val
    self.neighbors =[]

#or hashmap
adjList1 = {"A":[], "B":[]}

#given edges build a list
edges =[["A","B"],["B","C"], ["B","E"],["C","E"],["F","D"]]

adjList = {}

for src, dst in edges:
  if src not in adjList:
    adjList[src] = []
  if dst not in adjList:
    adjList[dst] = []
  adjList[src].append(dst)

print(adjList)