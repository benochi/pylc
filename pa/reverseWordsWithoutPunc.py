# Question: Implement a function to reverse words in a sentence while preserving whitespace.
# Method Signature: String reverseWords(String sentence)
# Expectations:
# Correctly reverse the order of words
# Preserve all whitespace, including leading and trailing spaces
# Handle sentences with multiple spaces between words


def reverseWords(s):
    if not s:
      return ""
    
    words = []
    spaces = []
    currWord = [] #store our current series of chars
    currSpace = [] #store our current series of spaces

    for char in s:
      if char.isspace():
        if currWord: #if we hit a space and have a series of chars join all chars and add space
          words.append("".join(currWord))
          currWord = []
        currSpace.append(char) #build series of spaces.
      else:
        if currSpace:
          spaces.append("".join(currSpace))
          currSpace = []
        currWord.append(char) #build series of chars

    if currWord:
      words.append(''.join(currWord))
    if currSpace:
      spaces.append(" ".join(currSpace))
    if s[0].isspace():
      words.append("")
    if not s[-1].isspace():
      spaces.append('')
    
    result = []
    words.reverse()

    for word, space in zip(words,spaces):
      result.append(word)
      result.append(space)
    
    return ''.join(result)
        

# Simple print tests
print(reverseWords("Hello World"))               # World Hello
print(reverseWords(" I have a lollipop "))       # lollipop a have I 
print(reverseWords("Double  Spaces"))            # Spaces  Double
print(reverseWords("Hello, world!"))             # world!, Hello
print(reverseWords(""))                          # (empty string)
print(reverseWords("   "))                       # (three spaces)
print(reverseWords("One"))                       # One
print(reverseWords("  Multiple   Spaces  "))     # Spaces   Multiple  