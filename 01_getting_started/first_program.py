"""
==============================================================================
Module: 01_getting_started / first_program.py
Description: The classical first program in Python, demonstrating fundamental
             syntax, printing, variables, comments, and execution entrypoint.
Author: Python Learning Hub
==============================================================================

To run this file:
    python3 first_program.py
"""


def main() -> None:
    # 1. Single-line comment: The hash '#' symbol is used for comments.
    # Python ignores anything after '#' on the same line.

    print("=" * 50)
    print("  🚀 Welcome to Python Learning Hub!")
    print("=" * 50)

    # 2. Basic Output with print()
    # print() displays messages or variables to the terminal/console.
    print("Hello, World! You are writing Python code.")

    # 3. Variables & Dynamic Typing
    # You do not need to declare data types explicitly.
    # Python infers the type dynamically at runtime.
    language_name = "Python"          # str (string / text)
    language_version = 3              # int (integer / whole number)
    learning_is_fun = True            # bool (boolean / True or False)
    rating = 9.9                      # float (floating-point number)

    # 4. Formatted Strings (f-strings)
    # Prefixing a string with 'f' allows embedding variables inside {curly_braces}.
    print(f"\nLearning: {language_name} (Major Version: {language_version})")
    print(f"Satisfaction Rating: {rating}/10 | Fun?: {learning_is_fun}")

    # 5. Type Inspection
    # The built-in type() function inspects what type an object is:
    print(f"Data type of 'language_name': {type(language_name).__name__}")
    print(f"Data type of 'language_version': {type(language_version).__name__}")

    # 6. Basic Arithmetic
    a = 15
    b = 4
    print(f"\nMath Demo:")
    print(f"{a} + {b} = {a + b} (Addition)")
    print(f"{a} - {b} = {a - b} (Subtraction)")
    print(f"{a} * {b} = {a * b} (Multiplication)")
    print(f"{a} / {b} = {a / b} (Float Division)")
    print(f"{a} // {b} = {a // b} (Floor / Integer Division)")
    print(f"{a} % {b} = {a % b} (Modulus / Remainder)")
    print(f"{a} ** 2 = {a ** 2} (Exponentiation / Power)")

    print("\n✅ Program executed successfully!")
    print("Ready to move to 02_python_fundamentals for variables, loops, and conditions!\n")


# Standard Python idiom to ensure code runs only when executed directly:
if __name__ == "__main__":
    main()
