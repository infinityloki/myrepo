import math

def is_prime(num):
    """
    Checks if a given number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 up to the square root of the number
    # We only need to check up to the square root because if a number 'n' has a divisor 'd' greater than sqrt(n),
    # then it must also have a divisor 'n/d' which is less than sqrt(n).
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  # If divisible, it's not prime

    return True  # If no divisors found, it's prime

# Example usage:
number_to_check = 29
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")

number_to_check_2 = 10
if is_prime(number_to_check_2):
    print(f"{number_to_check_2} is a prime number.")
else:
    print(f"{number_to_check_2} is not a prime number.")
