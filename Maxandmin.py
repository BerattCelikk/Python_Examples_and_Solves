# PROGRAM THAT FINDS MAX AND MIN IN ARRAY


length=int(input("enter length of the array :"))

array=[]

for i in range(length):
    element=int(input("enter a number :"))
    array.append(element)
    
max_number,min_number=array[0],array[0]

for i in range(length):
    if(max_number<array[i]):
        max_number=array[i]
    elif(min_number>array[i]):
        min_number=array[i]

print(f"max number = {max_number} and min number = {min_number}")