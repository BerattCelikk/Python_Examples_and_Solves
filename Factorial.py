#DISPLAY FACTORIAL VALUE OF N ENTERED BY THE USER

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
    
number=int(input("enter a number :"))
print(f"factorial of {number} = {factorial(number)} ")