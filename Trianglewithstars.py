#  PROGRAM THAT MAKING TRIANGLE WITH STARS

length = int(input("Enter length of the triangle: "))

for i in range(1, length + 1):

    for j in range(length - i):
        print(" ", end="")
    
    for k in range(i):
        print("*", end=" ")
    
    print()
