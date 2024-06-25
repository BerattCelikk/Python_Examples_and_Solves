#SPLIT EVEN AND ODD NUMBERS IN ARRAY.

length=int(input("enter length of the array :"))
array=[]
odd=[]
even=[]

for i in range(length):
    element=int(input("enter a number:"))
    array.append(element)
    if(element%2==1):
        odd.append(element)
    elif(element%2==0):
        even.append(element)
        
print(f"Original Array : {array}")
print(f"Odd Numbers : {odd}")
print(f"Even Numbers : {even}")

        


    
 