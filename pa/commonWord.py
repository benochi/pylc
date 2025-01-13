

def wordFinder(file):
  try:
    with open(file, 'r', encoding="utf-8") as fileHandler:
      count = {}

      for line in fileHandler:
        words = line.strip().split()
        for word in words:
          word.lower().strip(".,!?\"'")
          count[word] = count.get(word,0) + 1
    maxFrequency = max(count.values())
    frequentWords = []
    wordToReturn = None
    wordLen = 0
    for word, frequency in count.items():
      if frequency == maxFrequency:
        frequentWords.append(word)
    
    for word in frequentWords:
      if len(word) > wordLen:
        wordToReturn = word
        wordLen = len(word)
      print(ord(word[0]))

    print(wordToReturn)
  except FileNotFoundError:
    print(f"Filename: {file} not found.")
  
  except Exception as e:
    print(f"an error has occurred: {e}")

wordFinder("sample.txt")
                             