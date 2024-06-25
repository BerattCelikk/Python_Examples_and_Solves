#  PROGRAM THAT FINDS ARMSTRONG NUMBERS(EX: 1^3+5^3+3^3=153)(digit * number of digits)

number = int(input("Enter a number: "))

temp = number
counter = 0
while temp > 0:
    temp //= 10
    counter += 1

temp = number
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** counter
    temp //= 10

if sum == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
