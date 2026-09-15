"""
Program 8: Count word frequencies in a sentence using a dictionary
Concept: Dictionaries (creation, access, update) + Loops
"""

def count_word_frequencies(sentence):
    """Count the frequency of each word in a sentence.
    
    Args:
        sentence: Input string to analyze
        
    Returns:
        Dictionary with words as keys and their frequencies as values
    """
    # Convert to lowercase and split into words
    words = sentence.lower().split()
    
    # Create empty dictionary to store word counts
    word_count = {}
    
    # Count each word
    for word in words:
        # Remove punctuation from word
        word = word.strip('.,!?;:"()[]{}')
        if word:  # Only count non-empty words
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    return word_count

if __name__ == "__main__":
    # Test with sample sentence
    test_sentence = "test test demo"
    result = count_word_frequencies(test_sentence)
    print(f"Input: '{test_sentence}'")
    print(f"Word frequencies: {result}")