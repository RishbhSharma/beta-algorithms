def sieve_of_eratosthenes(x,n):
    prime=[True]*(n+1)
    prime[0]=prime[1]==False
    p=2
    while p*p<=n:
        if prime[p]:
            i=p*2
            while i<=n:
                prime[i]=False
                i+=p
        p+=1
    primes=[]
    for i in range(x,n+1):
        if prime[i]:
            print i
    print
for t in range(input()):
    i,j=map(int,raw_input().split())
    sieve_of_eratosthenes(i,j)
