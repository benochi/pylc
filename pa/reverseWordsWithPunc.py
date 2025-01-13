# Question: Implement a function to reverse words in a sentence while preserving whitespace.
# Method Signature: String reverseWords(String sentence)
# Expectations:
# Correctly reverse the order of words
# Preserve all whitespace, including leading and trailing spaces
# Handle sentences with multiple spaces between words


def reverseWords(sentence):
    if not sentence:
        return ""

    # First, identify word boundaries and spaces
    words = []
    spaces = []
    current_word = []
    current_space = []
    
    for char in sentence:
        if char.isspace():
            if current_word:
                words.append(''.join(current_word))
                current_word = []
            current_space.append(char)
        else:
            if current_space:
                spaces.append(''.join(current_space))
                current_space = []
            current_word.append(char)
            
    # Handle any remaining word or space
    if current_word:
        words.append(''.join(current_word))
    if current_space:
        spaces.append(''.join(current_space))
    
    # If the sentence starts with a space, we need an extra empty word at the end
    if sentence[0].isspace():
        words.append('')
    
    # If the sentence ends with a word, we need an extra empty space
    if not sentence[-1].isspace():
        spaces.append('')
        
    # Reverse the words
    words.reverse()
    
    # Reconstruct the sentence by interleaving words and spaces
    result = []
    for word, space in zip(words, spaces):
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