def greet(name):
    """Print a greeting message."""
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello!")

def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b

def main():
    """Main function."""
    user_name = input("Enter your name: ")
    greet(user_name)

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

