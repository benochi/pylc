

def carBridge(u, weights):
  n = len(weights)
  turnBacks = 0
  w = 0 
  while w < n - 1:
    if weights[w] + weights[w + 1] > u:
      turnBacks += 1
      w += 1
    else:
      w += 1
  if weights[-1] > u:
    turnBacks += 1
      

  return turnBacks

print(carBridge(u = 9, weights = [5, 3, 8, 1, 8, 7, 7, 6])) # 4
print(carBridge(u = 7, weights = [7, 6, 5, 2, 7, 4, 5, 41])) # 5
print(carBridge(u = 7, weights = [3, 4, 3, 1])) #0
print(carBridge(u = 2, weights = [3, 7, 5, 5, 6, 3, 9, 10, 8, 4])) #10