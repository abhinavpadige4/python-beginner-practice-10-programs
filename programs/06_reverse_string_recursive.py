"""
Program 6: Recursive string reversal
Concept: Recursion (base case, recursive step)
"""

def reverse_string(s):
    """Reverse a string using recursion.
    
    Args:
        s: String to reverse
        
    Returns:
        Reversed string
    """
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    # Recursive step: last char + reverse of remaining string
    else:
        return s[-1] + reverse_string(s[:-1])

if __name__ == "__main__":
    # Test with input 'hello'
    test_string = "hello"
    result = reverse_string(test_string)
    print(f"Original: '{test_string}'")
    print(f"Reversed: '{result}'")