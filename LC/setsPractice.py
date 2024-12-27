#practice for some sets

def setStuff(arr):
  #add, remove, discard(no error if it doesn't exist), pop, clear, union, intersection, difference
  set1 = set(arr[1:7])
  set2 = set(arr[7:])
  set3 = set(arr[7:])
    
  set1.add(("Hello", "World"))
  set1.remove(6)
  set1.discard(("Doesn't", "Exist"))
  s = set1.pop()
  print(s)
  set3.clear()
  set4 = set1.union(set2)
  #coerce set into list
  list1 = list(set4)
  set5 = set1.intersection(set2)
  set6 = set1.difference(set2)

  return set1, set2, set3, set4, list1, set5, set6





print(setStuff([1,2,3,4,5,5,6,2,3,5,7,8,5,6]))