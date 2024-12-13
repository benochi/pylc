from collections import deque


class GraphNode:
  def __init__(self,val):
    self.val = val
    self.neighbors =[]

#or hashmap
adjList1 = {"A":[], "B":[]}

#given edges build a list
edges =[["A","B"],["A","D"],["B","C"], ["B","E"],["C","E"],["F","D"], ["D","E"]]

adjList = {}

for src, dst in edges:
  if src not in adjList:
    adjList[src] = []
  if dst not in adjList:
    adjList[dst] = []
  adjList[src].append(dst)

#DFS on adjList W backtracking exponential
def dfs(node, target, adjList, visit):
  if node in visit:
    return 0
  if node == target:
    return 1
  
  count = 0
  visit.add(node)
  for neighbor in adjList[node]:
    count += dfs(neighbor, target, adjList, visit)
  visit.remove(node) #backtracking

  return count

def bfs(node, target, adjList):
  length = 0
  visit = set()
  visit.add(node)
  q = deque(node)

  while q:
    for i in range(len(q)):
      curr = q.popleft()
      if curr == target:
        return length

      for neighbor in adjList[curr]:
        if neighbor not in visit:
          visit.add(neighbor)
          q.append(neighbor)
    length += 1
  return length


print(dfs("A","E", adjList, set()))
print(bfs("A","E", adjList))

print(adjList)