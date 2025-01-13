def reverse_words(sentence: str) -> str:
    if not sentence:
        return sentence
        
    # Step 1: Split the sentence into words and spaces
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
            
    # Handle the last word or space
    if current_word:
        words.append(''.join(current_word))
    if current_space:
        spaces.append(''.join(current_space))
        
    # Handle case where sentence starts with space
    if sentence[0].isspace():
        # Add empty string at start of words to maintain index alignment
        words.insert(0, '')
    
    # Handle case where sentence ends with non-space
    if not sentence[-1].isspace():
        spaces.append('')

    
    # Step 3: Reconstruct the sentence
    result = []
    for i in range(len(spaces)):
        result.append(words.pop())
        result.append(spaces[i])
        
    return ''.join(result)

# Test cases
def test_reverse_words():
    test_cases = [
        "Hello   World",
        "  Hello World  ",
        "One",
        "   ",
        "",
        "First   Second     Third",
        "  Multiple   Spaces   Between   Words  "
    ]
    
    for test in test_cases:
        result = reverse_words(test)
        print(f"Input: '{test}'")
        print(f"Output: '{result}'")
        print("-" * 50)

if __name__ == "__main__":
    test_reverse_words()