
def uniqueStr(str):
  count = {}
  for c in str:
    count[c] = count.get(c, 0) + 1
  
  size = len(count)
  
  l = 0
  currMap = {}
  curLen = 0
  curStr = ""
  winStart = 0

  for c in str:
    currMap[c] = currMap.get(c, 0) + 1
    curStr += c
    curLen += 1
    while len(currMap) == size:
      if c - l + 1 < curLen:
        curLen = c - l + 1
        winStart = l

      currMap[str[l]] -= 1
      if currMap[str[l]] == 0:
          curLen -= 1
      l += 1
      

  print(currMap.values())






print(uniqueStr("abcdbbccddaadd"))