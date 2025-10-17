# -*- coding: utf-8 -*-

def func1():
    s = input()
    print(s.count(" е"))

def func2():
    s = input()
    print(s.replace(":","%"), s.count(":"), sep="\n")

def func3():
    s = input()
    print(s.replace(".",""), s.count("."), sep="\n")

def func4():
    s = input()
    print(s.replace("а","о"), s.count("а"), len(n), sep="\n")

def func5():
    s = input()
    print(s.lower())

def func6():
    s = input()
    print(s.replace("а",""), s.count("а"), sep="\n")

def func7():
    s = input()
    print("".join([s[:len(s)//2:].replace("п","*"),s[len(s)//2::]]), s.count("п"), sep="\n")

def func8():
    s = input()
    print(s.count(" "))

def func9():
    s = input()
    print(s.count(input()), sep="\n")

def func10():
    s = input()
    a = []
    for i in s.split(" "):
        a.append(i.replace(i[0],i[0].upper()))
    print(" ".join(a))

def func11():
    s = input()
    c = 0
    m = 0
    for i in s:
        if i == "н":
            c += 1
        else:
            m = c if m > c else m
            c = 0
    print(s.replace("!","."), m, sep="\n")

def func12():
    s = input()
    n = ""
    for i in s.split(" "):
        if i[-1] == "я":
            n += i + " "
    print(n)

def func13():
    s = input()
    print(s[s.find("(") + 1:s.find(")"):])

def func14():
    s = input()
    n = ""
    for i in s.split(" "):
        if i[-1] == "я" or i[0] == "а":
            n += i + " "
    print(n)

def func15():
    s = input()
    print(s.count("т"))
