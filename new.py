
print("hello world")
a=100
print("hello world")

print("test  first  changes --Ajinkya")

#code start
# Simple 50-line Python Test Script

# 1. Import modules
import random

# 2. Function to generate random numbers
def generate_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

# 3. Function to calculate average
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# 4. Function to find even and odd numbers
def split_even_odd(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    return evens, odds

# 5. Function to write results to file
def write_to_file(filename, data):
    with open(filename, "w") as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

# 6. Function to read and display file content
def read_file(filename):
    with open(filename, "r") as f:
        print("\n--- File Content ---")
        print(f.read())

# 7. Main program
def main():
    print("Simple Python Test Program")

    # Generate 10 random numbers
    numbers = generate_numbers(10)
    print("Numbers:", numbers)

    # Calculate statistics
    avg = calculate_average(numbers)
    evens, odds = split_even_odd(numbers)

    # Display results
    print(f"Average: {avg:.2f}")
    print("Even Numbers:",
# code end
