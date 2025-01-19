# Question: Write a program to find the n most frequent words in a large text file.
# Method Signature: List<String> mostFrequentWords(String filePath, int n)
# Expectations:
# Efficiently read and process large files
# Handle ties and case sensitivity

import heapq

def fileSearch(file_path, n):
  count = {}

  with open(file_path, 'r') as file:
    for line in file:
      words = line.strip().split()
      for word in words:
        word = word.lower().strip(".,!\"'")
        count[word] = count.get(word, 0) + 1
        
  maxHeap= []
  result = []
  for word, freq in count.items():
    heapq.heappush(maxHeap, (-freq, word))

  for i in range(min(n, len(maxHeap))):
    freq, word = heapq.heappop(maxHeap)
    result.append(word)

  return result

print(fileSearch("sample.txt", 4))