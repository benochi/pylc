# Question: Implement a function to reverse words in a sentence while preserving whitespace.
# Method Signature: String reverseWords(String sentence)
# Expectations:
# Correctly reverse the order of words
# Preserve all whitespace, including leading and trailing spaces
# Handle sentences with multiple spaces between words


def reverseWords(sentence):
    if not sentence:
        return ""

    words = []
    non_words = []  # spaces and punctuation
    current_word = []
    current_non_word = []
    
    for char in sentence:
        if char.isspace() or not char.isalnum():  # space or punctuation
            if current_word:
                words.append(''.join(current_word))
                current_word = []
            current_non_word.append(char)
        else:
            if current_non_word:
                non_words.append(''.join(current_non_word))
                current_non_word = []
            current_word.append(char)
            
    # Handle any remaining chunks
    if current_word:
        words.append(''.join(current_word))
    if current_non_word:
        non_words.append(''.join(current_non_word))
    
    # If the sentence starts with non-word, we need an extra empty word at the end
    if not sentence[0].isalnum():
        words.append('')
    
    # If the sentence ends with word, we need an extra empty non-word
    if sentence[-1].isalnum():
        non_words.append('')
        
    words.reverse()
    
    # Reconstruct the sentence by interleaving
    result = []
    for word, non_word in zip(words, non_words):
        result.append(word)
        result.append(non_word)
        
    return ''.join(result)
        

# Simple print tests
print(reverseWords("Hello World"))               # World Hello
print(reverseWords(" I have a lollipop "))       # lollipop a have I 
print(reverseWords("Double  Spaces"))            # Spaces  Double
print(reverseWords("Hello, world!"))             # world, Hello!
print(reverseWords(""))                          # (empty string)
print(reverseWords("   "))                       # (three spaces)
print(reverseWords("One"))                       # One
print(reverseWords("  Multiple   Spaces  "))     # Spaces   Multiple  
print(reverseWords("..Multiple,, punctuations!!"))     # Spaces   Multiple  