def fact(int n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
a=int(input("enter a number: "))
print(fact(a))
