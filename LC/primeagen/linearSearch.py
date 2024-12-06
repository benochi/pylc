def linearSearch(haystack, needle):
  for h in haystack:
    if h == needle:
      return True
    
  return False
  
print(linearSearch([1,2,3,4,5,6,7], 7))
print(linearSearch([1,2,3,4,5,6,7], 0))
print(linearSearch([1,2,3,4,5,6,7], -1))