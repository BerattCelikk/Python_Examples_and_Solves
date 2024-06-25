# PROGRAM THAT FINDS POLINDROME NUMBERS (EX: 14641 , 1001 , 32123) (remains same when its digits are reversed.)

def is_palindrome(number):
    original_number = number
    reversed_number = 0
    
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10  # Tam sayı bölme
    
    return original_number == reversed_number

number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome number")
else:
    print(f"{number} is not a palindrome number")
