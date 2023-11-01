myList = [i for i in range(10)]

print(myList)

def fib(lim):
    a,b = 0,1
    while a<lim:
        yield a
        a,b = b,a+b

myFib = fib(10)

for i in myFib:
    print(i)