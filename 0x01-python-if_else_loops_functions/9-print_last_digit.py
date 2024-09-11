def print_last_digit(number):
    # Find the last digit by taking the absolute value and getting the remainder when divided by 10
    last_digit = abs(number) % 10
    # Print the last digit
    print(last_digit, end="")
    # Return the last digit
    return last_digit
