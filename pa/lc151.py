def reverseWords(s):
  words = s.split()
  reversed = []
  #reversed_words = words[::-1]

  for i in reversed(words):
        reversed.append(words[i])

  result = " ".join(reversed)
  return result

print(reverseWords(" Hello World! "))
print(reverseWords("  Double  Spaces  "))