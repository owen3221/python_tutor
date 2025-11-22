# Homework: Lecture 0 - Functions & Variables
# Students: Fill in the TODO parts
# Run this file with python homework_lec0.py
# The program will check your answers automatically.

# 1. Define a function that greets the user by name
def greet(name: str) -> str:
    # TODO: return a string like "Hello, Alice!"
    pass


# 2. Define a function that returns the sum of two numbers
def add(a: int, b: int) -> int:
    # TODO: return a + b
    pass


# 3. Define a function that squares a number
def square(x: int) -> int:
    # TODO: return x squared
    pass


# 4. Define a function that converts Celsius to Fahrenheit
def c_to_f(c: float) -> float:
    # TODO: return Celsius converted to Fahrenheit (F = C * 9/5 + 32)
    pass


# 5. Define a function that returns True if a number is even, False otherwise
def is_even(n: int) -> bool:
    # TODO: return True if n is divisible by 2
    pass


# 6. Please Start from the beginning a function named average 
#    It should return the average of two numbers (a + b) / 2



# ============================
# DO NOT CHANGE THE CODE BELOW
# ============================

def main():
    score = 0
    total = 6

    # Test greet
    if greet("Alice") == "Hello, Alice!":
        score += 1
    else:
        print(" greet('Alice') should return 'Hello, Alice!'")

    # Test add
    if add(3, 4) == 7:
        score += 1
    else:
        print(" add(3, 4) should return 7")

    # Test square
    if square(5) == 25:
        score += 1
    else:
        print(" square(5) should return 25")

    # Test c_to_f
    if abs(c_to_f(0) - 32.0) < 1e-6 and abs(c_to_f(100) - 212.0) < 1e-6:
        score += 1
    else:
        print(" c_to_f conversion is wrong")

    # Test is_even
    if is_even(4) is True and is_even(5) is False:
        score += 1
    else:
        print(" is_even function is wrong")

    # Test average
    if abs(average(4, 6) - 5.0) < 1e-6 and abs(average(10, 20) - 15.0) < 1e-6:
        score += 1
    else:
        print("❌ average function is wrong")

    print(f"\n✅ You got {score}/{total} correct!")


if __name__ == "__main__":
    main()