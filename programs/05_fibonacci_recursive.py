"""
Program 5: Recursive Fibonacci (nth term)
Concept: Recursion (base case, recursive step)
"""

def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        nth Fibonacci number
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive step: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    # Test with Fibonacci of 7 (should return 13)
    n = 7
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")