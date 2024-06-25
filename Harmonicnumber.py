# PROGRAM THAT CALCULATE HARMONIK AVERAGE UP TO N.(USER WİLL ENTER THE N).

n=int(input("enter a number :"))

sum=0
for a in range(1,n):
    sum+=(1/a)
    
harmonic=(n/sum)
harmonic=round(harmonic,3)
print(f"Harmonic Average = {harmonic}")