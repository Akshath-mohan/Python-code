# WAP to find out the number is palindrome or not using function

def is_palindrome(number):
    num_str = str(12321)
    return num_str == num_str[::-1]

#number = 12321

if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")