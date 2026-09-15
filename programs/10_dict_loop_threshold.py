"""
Program 10: Loop over dictionary to find keys with values above threshold
Concept: Dictionaries (access, iteration) + Loops
"""

def find_keys_above_threshold(scores, threshold):
    """Find all keys in a dictionary where values are above a given threshold.
    
    Args:
        scores: Dictionary with keys and numeric values
        threshold: Minimum value threshold
        
    Returns:
        List of keys where corresponding values are above threshold
    """
    result = []
    
    # Loop through dictionary items
    for key, value in scores.items():
        if value > threshold:
            result.append(key)
    
    return result

if __name__ == "__main__":
    # Test with sample dictionary of scores
    test_scores = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 96,
        "Eve": 83,
        "Frank": 79
    }
    
    threshold = 80
    high_scorers = find_keys_above_threshold(test_scores, threshold)
    
    print(f"Scores: {test_scores}")
    print(f"Threshold: {threshold}")
    print(f"Keys with values above {threshold}: {high_scorers}")
    
    # Alternative test with different threshold
    print()
    threshold_2 = 90
    high_scorers_2 = find_keys_above_threshold(test_scores, threshold_2)
    print(f"Keys with values above {threshold_2}: {high_scorers_2}")