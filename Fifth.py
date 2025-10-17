def func1():
    N = int(input())
    i = 1
    while i**2 <= N:
        print(i**2)
        i += 1

def func2():
    N = int(input())
    i = 2
    while N % i != 0:
        i += 1
    print(i)

def func3():
    N = int(input())
    i = -1
    p = 1
    while p < N:
        i += 1
        p *= 2
    print(f"2**{i} = {p//2}")

def func4():
    x = float(input())
    y = float(input())
    d = 1
    while x < y:
        x *= 1.1
        d += 1
    print(d)

def func5():
    arr = []
    while True:
        i = int(input())
        if i == 0: break
        arr.append(i)
    print(len(arr))

def func6():
    s = 0
    n = 0
    while True:
        i = float(input())
        if i == 0: break
        s += i
        n += 1
    print(i/n)

def func7():
    j = int(input())
    s = 0
    while True:
        i = int(input())
        if i == 0: break
        if j < i: s += 1
        j = i
    print(s)

def func8():
    j = int(input())
    s = 0
    m = 0
    while True:
        i = int(input())
        if i == 0: break
        if j == i:
            s += 1
        else:
            m = s if m < s else m
            s = 0
    print(m)