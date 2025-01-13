from collections import Counter
from typing import List
import re
from itertools import takewhile
import heapq
from pathlib import Path

class WordFrequencyFinder:
    def __init__(self, chunk_size: int = 8192, case_sensitive: bool = False):
        """
        Initialize the word frequency finder.
        
        Args:
            chunk_size: Size of chunks to read from file
            case_sensitive: Whether to treat words case-sensitively
        """
        self.chunk_size = chunk_size
        self.case_sensitive = case_sensitive
        # Regex for word boundaries, including apostrophes for contractions
        self.word_pattern = re.compile(r"[a-zA-Z]+(?:'[a-zA-Z]+)?")
    
    def process_chunk(self, text: str) -> List[str]:
        """Process a chunk of text into words."""
        words = self.word_pattern.findall(text)
        if not self.case_sensitive:
            words = [word.lower() for word in words]
        return words
    
    def stream_words(self, file_path: str):
        """Generator to stream words from file in chunks."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        leftover = ""
        with path.open('r', encoding='utf-8') as file:
            while True:
                chunk = file.read(self.chunk_size)
                if not chunk:
                    # Process any remaining text
                    if leftover:
                        yield from self.process_chunk(leftover)
                    break
                
                # Combine with leftover from previous chunk
                text = leftover + chunk
                
                # Find last space to avoid splitting words
                last_space = text.rfind(' ')
                if last_space == -1:
                    # No space found, process entire chunk
                    yield from self.process_chunk(text)
                    leftover = ""
                else:
                    # Process up to last space
                    yield from self.process_chunk(text[:last_space])
                    leftover = text[last_space:]

    def most_frequent_words(self, file_path: str, n: int) -> List[tuple[str, int]]:
        """
        Find n most frequent words in the file.
        
        Returns list of (word, frequency) tuples.
        Handles ties by including all words with same frequency as nth word.
        """
        if n < 1:
            raise ValueError("n must be positive")
            
        # Count word frequencies
        counter = Counter()
        for word in self.stream_words(file_path):
            counter[word] += 1
            
        if not counter:
            return []
            
        # Get n most common words
        most_common = counter.most_common()
        
        # Handle ties - include all words with same frequency as nth word
        if n < len(most_common):
            nth_freq = most_common[n-1][1]
            result = list(takewhile(lambda x: x[1] >= nth_freq, most_common))
        else:
            result = most_common
            
        return result

def test_word_frequency():
    # Create a test file
    test_file = "test_text.txt"
    test_content = """
    The quick brown fox jumps over the lazy dog.
    The dog sleeps while the fox jumps.
    The quick brown fox is quick and brown.
    """
    
    with open(test_file, 'w') as f:
        f.write(test_content)
    
    # Test with different configurations
    finder = WordFrequencyFinder(case_sensitive=False)
    
    # Test case 1: Basic functionality
    result = finder.most_frequent_words(test_file, 3)
    print("Top 3 words:")
    for word, count in result:
        print(f"{word}: {count}")
    
    # Test case 2: Case sensitivity
    finder_case = WordFrequencyFinder(case_sensitive=True)
    result_case = finder_case.most_frequent_words(test_file, 3)
    print("\nTop 3 words (case sensitive):")
    for word, count in result_case:
        print(f"{word}: {count}")
    
    # Clean up test file
    Path(test_file).unlink()

if __name__ == "__main__":
    test_word_frequency()