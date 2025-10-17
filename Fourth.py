#1
def requiem():
    a = int(input("a = "))
    b = int(input("b = "))
    if a>b:
		requiem()
		return
    for i in range(a,b+1,1):
		print(i)

#requiem()

#2
def nonsence():
    a = int(input("a = "))
    b = int(input("b = "))
    s = 1 if a < b else -1
    for i in range(a,b+s,s):
		print(i)

#nonsence()

#3
def odds():
    a = int(input("a = "))
    b = int(input("b = "))
    for i in filter(lambda x: x%2==1, range(a,b+1,1)):
		print(i)

#odds()

#4
def sum_of_N():
	s = 0
	for i in range(1, int(input("N = ")) + 1):
		s += int(input("N" + str(i) + " = "))
	print(s)

#sum_of_N()

#5
def sum_of_cubes():
	s = 0
	for i in range(1, int(input("n = ")) + 1):
		s += i**3
	print(s)

#sum_of_cubes()

#6
def factorial():
	f = 1
	for i in range(1, int(input("n = ")) + 1):
		f *= i
	print(f)

#factorial()

#7
def sum_of_factorials():
	s = 0
	f = 1
	for i in range(1, int(input("n = ")) + 1):
		f *= i
		s += f
	print(s)

#sum_of_factorials()

#8
def ladders():
	n = int(input("n = "))
	if n > 9:
		ladders()
		return
	for k in range(1, n + 1):
		s = ""
		for i in range(1, k + 1):
			s += str(i)
		print(s)

#ladders()

#9
def sum_of_fibonachi():
	f = [0,1]
	s = 0
	for i in range(int(input("N = "))):
		f.append(f[i] + f[i + 1])
		s += f[i]
	print(s)

#sum_of_fibonachi()

#10
def sum_of_fibonachi_2():
	f = [0,1]
	s = 0
	n = int(input("N = "))
	k = int(input("K = "))
	for i in range(n):
		f.append(f[i] + f[i + 1])
		if i < k-1:
			continue
		s += f[i]
	print(s)

#sum_of_fibonachi_2()
