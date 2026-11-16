# number_converter.py
# A Python program to convert decimal numbers to binary and hexadecimal representations.

def convert_number():
    try:
        # Prompt the user to enter a decimal number
        user_input = input("Enter a positive decimal number: ")
        decimal_num = int(user_input)
        
        if decimal_num < 0:
            print("Please enter a positive integer.")
            return
            
        # Convert using built-in bin() and hex() functions
        binary_output = bin(decimal_num)
        hex_output = hex(decimal_num)
        
        # Display the results
        print(f"Decimal: {decimal_num}")
        print(f"Binary: {binary_output}")
        print(f"Hexadecimal: {hex_output}")
        
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")

if __name__ == "__main__":
    convert_number()