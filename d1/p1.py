# Question: Implement a function to reverse words in a sentence while preserving whitespace.
# Method Signature: String reverseWords(String sentence)
# Expectations:
# Correctly reverse the order of words
# Preserve all whitespace, including leading and trailing spaces
# Handle sentences with multiple spaces between words


def reverseWords(sentence):
  if not sentence:
    return ''
  
  words = []
  non_words = []
  curr_word = []
  curr_non_word = []
  
  #arrays for words, non_words, curr_word, curr_non_word
  for char in sentence:
    if char.isspace() or not char.isalnum():
      if curr_word:
        words.append(''.join(curr_word))
        curr_word = []
      curr_non_word.append(char)
    else:
      if curr_non_word:
        non_words.append(''.join(curr_non_word))
        curr_non_word = []
      curr_word.append(char)
    
  if curr_word:
    words.append(''.join(curr_word))
  if curr_non_word:
    non_words.append(''.join(curr_non_word))

  if not sentence[0].isalnum():
    words.append('')
  if sentence[-1].isalnum():
    non_words.append('')

  words.reverse()
  result = []
  for word, non_word in zip(words, non_words):
    result.append(word)
    result.append(non_word)

  return ''.join(result)


print(reverseWords("  Hello World  "))
print(reverseWords("  Hello  World  "))
print(reverseWords("  Hello  World 1"))
