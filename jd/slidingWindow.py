def wacky(str):
  count = Counter(str)
  distinct = {}
  l = 0
  smallestWindow = float('inf')
  minWindow = ""

  for r, c in enumerate(str):
        if c in distinct:
            distinct[c] += 1
        else:
            distinct[c] = 1

        while len(distinct) == len(count):
            if r - l + 1 < smallestWindow:
                smallestWindow = r - l + 1
                minWindow = str[l:r+1]

            distinct[str[l]] -= 1
            if distinct[str[l]] == 0:
                del distinct[str[l]]
            l += 1

  return minWindow

print(wacky("aabcbcdbca")) #dbca
print(wacky("aaab")) #ab