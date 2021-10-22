n=float(input("Enter a number: "))
if n>1:
    for i in range(2, n//2):
        if(n%i)==0:
            print(n,": False")
            break
    else:
        print(n,": True")
else:
    print(n,"Invalid")