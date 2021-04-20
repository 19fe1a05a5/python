def evenorodd(a):
    if(a%2==0):
        print("a is even")
    else:
        print("a is odd")
#evenorodd(n)

def primes(n):
    count=0
    for i in range(2,n+1):
        if(n%i==0):
            count+=1
    if(count==1):
        print(" prime")
    else:
        print("  not prime")
#primes(n)