# 1. Function for Basic Operations: Sum, Difference, Product, Quotient
def basic_operations(num1, num2):
    """
    This function performs basic operations on two numbers:
    - Sum
    - Difference
    - Product
    - Quotient (division)
    """
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    if num2 != 0:  # Check to avoid division by zero
        quotient_result = num1 / num2
    else:
        quotient_result = "undefined (cannot divide by zero)"
    
    return sum_result, difference_result, product_result, quotient_result

# 2. Function to Calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    """
    This function calculates the simple interest using the formula:
    Simple Interest = (Principal * Rate * Time) / 100
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# 3. Function to Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    This function converts Celsius to Fahrenheit using the formula:
    Fahrenheit = (9/5 * Celsius) + 32
    """
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

# Main function to interact with the user
def main():
    # 1. Get user input for basic operations
    print("Basic Operations:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum_result, difference_result, product_result, quotient_result = basic_operations(num1, num2)
    
    # Display the results
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")
    print(f"Product: {product_result}")
    print(f"Quotient: {quotient_result}")
    print("-" * 30)
    
    # 2. Get user input for Simple Interest calculation
    print("Simple Interest Calculation:")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (in %): "))
    time = float(input("Enter the time period (in years): "))
    interest = calculate_simple_interest(principal, rate, time)
    
    # Display the calculated interest
    print(f"Simple Interest: {interest}")
    print("-" * 30)
    
    # 3. Get user input for Temperature Conversion
    print("Temperature Conversion (Celsius to Fahrenheit):")
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = convert_to_fahrenheit(celsius)
    
    # Display the converted temperature
    print(f"Temperature in Fahrenheit: {fahrenheit}")

# Ensure the program runs only when executed directly

main()
