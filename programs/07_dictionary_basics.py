"""
Program 7: Dictionary basics - create, access, update, delete a student record
Concept: Dictionaries (creation, access, update, deletion)
"""

def demonstrate_dictionary_basics():
    """Demonstrate basic dictionary operations."""
    # Create a student record dictionary
    student = {
        "name": "Alice Johnson",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8
    }
    
    print("Initial student record:")
    print(student)
    print()
    
    # Access values
    print("Accessing values:")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"GPA: {student['gpa']}")
    print()
    
    # Update values
    print("Updating values...")
    student["age"] = 21
    student["gpa"] = 3.9
    student["year"] = "Junior"  # Adding new key-value pair
    print("After updates:")
    print(student)
    print()
    
    # Delete values
    print("Deleting 'major' key...")
    del student["major"]
    print("After deletion:")
    print(student)
    print()
    
    # Check if key exists
    print("Checking if keys exist:")
    print(f"'name' in student: {'name' in student}")
    print(f"'major' in student: {'major' in student}")

if __name__ == "__main__":
    demonstrate_dictionary_basics()