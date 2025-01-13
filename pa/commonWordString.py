def wordFinder(inputString):
    try:
        # Ensure input is a valid string
        if not isinstance(inputString, str):
            raise ValueError("Input must be a valid string.")

        count = {}

        # Process each line in the input string
        lines = inputString.splitlines()
        for line in lines:
            words = line.strip().split()
            for word in words:
                word = word.lower().strip(".,!?\"'")
                count[word] = count.get(word, 0) + 1

        # Find the maximum frequency
        maxFrequency = max(count.values())
        frequentWords = []
        wordToReturn = None
        wordLen = 0

        # Collect all most frequent words
        for word, frequency in count.items():
            if frequency == maxFrequency:
                frequentWords.append(word)

        # Find the longest word among the most frequent
        for word in frequentWords:
            if len(word) > wordLen:
                wordToReturn = word
                wordLen = len(word)

        # Print the most frequent words and their counts
        print("Most Frequent Words and Counts:")
        for word in frequentWords:
            print(word, count[word])

        print("Longest Frequent Word:", wordToReturn)

    except Exception as e:
        print(f"An error has occurred: {e}")


# Example Usage
long_string = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

wordFinder(long_string)