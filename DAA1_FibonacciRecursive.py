# fibonacciseries (B)

COUNT=0
def recur_fibo(n):
    global COUNT
    COUNT=COUNT+1
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms=int(input("How Many Terms?"))
if nterms<=0:
    print("Please enter positive integer...")
else:
    print("Fibonacci Sequence:")
    for i in range (nterms):
        print(recur_fibo(i))
print("Steps Required using Counter: ",COUNT)