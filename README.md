# Python Beginner Practice: 10 Programs

This repository contains 10 Python practice programs designed for beginners to learn and practice:
- Loops (for/while, nested loops)
- Recursion (base case, recursive step)
- Dictionaries (creation, access, update, deletion, nesting)

## Programs Included

1. **01_print_numbers.py** - Simple for-loop to print numbers 1 to 10
   - Concept: Basic for loop iteration
   - Output: Numbers 1 through 10, each on a new line

2. **02_sum_while.py** - While-loop to compute sum of a list of integers
   - Concept: While loop with counter
   - Output: Sum of [5, 10, 15] = 30

3. **03_multiplication_table.py** - Nested for-loops to print a multiplication table (1-10)
   - Concept: Nested loops
   - Output: 10x10 multiplication table

4. **04_factorial_recursive.py** - Recursive factorial function
   - Concept: Recursion with base case
   - Output: Factorial of 5 = 120

5. **05_fibonacci_recursive.py** - Recursive Fibonacci (nth term)
   - Concept: Recursion with multiple base cases
   - Output: Fibonacci(7) = 13

6. **06_reverse_string_recursive.py** - Recursive string reversal
   - Concept: Recursion on strings
   - Output: "hello" reversed to "olleh"

7. **07_dictionary_basics.py** - Dictionary basics: create, access, update, delete a student record
   - Concept: Dictionary CRUD operations
   - Output: Demonstrates creating, reading, updating, and deleting dictionary entries

8. **08_word_frequency.py** - Count word frequencies in a sentence using a dictionary
   - Concept: Dictionary accumulation + string processing
   - Output: "test test demo" → {'test': 2, 'demo': 1}

9. **09_nested_dict_inventory.py** - Nest dictionaries: inventory of products with price and stock
   - Concept: Nested dictionaries
   - Output: Product inventory management with access, updates, and additions

10. **10_dict_loop_threshold.py** - Loop over dictionary to find keys with values above threshold
    - Concept: Dictionary iteration + conditional logic
    - Output: Finds students with scores above 80

## How to Run

Each program is a standalone Python file. To run any program:

```bash
python programs/01_print_numbers.py
```

Replace `01_print_numbers.py` with the program number you want to run.

To run all programs sequentially:

```bash
for i in {01..10}; do
    echo "Running program $i:"
    python programs/${i}_*.py
    echo "---"
done
```

## Topics Covered

- **Loops**: for loops, while loops, nested loops
- **Recursion**: base cases, recursive steps, factorial, Fibonacci, string reversal
- **Dictionaries**: creation, access, update, deletion, nesting, word frequency counting

## Requirements

- Python 3.8+

## Learning Path

These programs progress from simple concepts to more complex ones, helping beginners build a strong foundation in Python programming fundamentals. Each program includes:
- Clear problem statement
- Well-commented solution code
- Concept explanation
- Test case with expected output

## GitHub Repository Structure

```
python-beginner-practice-10-programs/
├── .gitignore
├── README.md
└── programs/
    ├── 01_print_numbers.py
    ├── 02_sum_while.py
    ├── 03_multiplication_table.py
    ├── 04_factorial_recursive.py
    ├── 05_fibonacci_recursive.py
    ├── 06_reverse_string_recursive.py
    ├── 07_dictionary_basics.py
    ├── 08_word_frequency.py
    ├── 09_nested_dict_inventory.py
    └── 10_dict_loop_threshold.py
```