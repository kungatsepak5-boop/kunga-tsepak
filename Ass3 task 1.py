num=int(input("Enter a number:"))
fac=1
if num <0:
    print ("invalid Input")
else:
    number=num
    while num>0:
        fac*=num
        num-=1
print(f"Factorial of {number} is :  {fac}")