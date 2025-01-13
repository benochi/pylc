def reverseWords(s):
  words = s.split()
  reversed = []
  
  for i in range(len(words) - 1, -1, -1):
        reversed.append(words[i])

  result = " ".join(reversed)
  return result