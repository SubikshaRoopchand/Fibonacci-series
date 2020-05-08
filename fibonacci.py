n=int(input("Enter a number:"))
f1=0
f2=1
for i in range(1,n):
    f3=f1+f2
    print(f1)
    f1=f2
    f2=f3
