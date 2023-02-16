def squares():
    n=int(input())
    a=(int(i)**2 for i in range(0,n))
    for i in range(n):
        print(next(a))

def evens():
    n=int(input())
    a=(int(i) for i in range(0, n, 2))
    for i in range(int(n/2)):
        print(next(a), end = ", ")
    print(next(a))

def devesibility():
    n = int(input())
    x = lambda x : x if (x % 3 == 0 and x % 4 == 0) or x == 0 else "o"
    a = (x(i) for i in range(0, n))
    for i in range(n):
        y = next(a)
        if(y != "o"):
            print(y)

def squaresFromAtoB():
    a = int(input())
    b = int(input())
    gen = (int(i)**2 for i in range(a, b + 1))
    for i in range((b-a) + 1):
        print(next(gen))

def decreasing():
    n = int(input())
    a = (i for i in range(n, 0, -1))
    for i in range(n):
        print(next(a))
