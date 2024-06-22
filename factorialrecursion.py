n = int(input("enter a no."))
def fibonacci(n):
    if (n==1 and n==0):
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
a = fibonacci(n)
print(a)