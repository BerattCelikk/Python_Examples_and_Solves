# a-)SORT FROM LARGEST TO SMALLEST

length=int(input("enter length of the array: "))

array=[]

for i in range(length):
    element=input(f" Enter {i+1}. element: ")
    array.append(element)

temp=0
for i in range(length):
    for j in range(0,length-i-1):
        if(array[j]<array[j+1]):
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
            
print("Largest to Smallest :")
for i in range(length):
    print(array[i]+" ")