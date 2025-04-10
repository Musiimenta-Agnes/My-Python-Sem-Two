import math

def my_name(name):
    return name





# Qn.
# Below is a Python code that defines a class with a constructor, creates an instance, and calls the method from that instance:

class MyClass:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Create an instance of MyClass
person = MyClass("Alice", 30)

# Call the greet method
message = person.greet()

# Output the result
print(message)
