# -*- coding: utf-8 -*-

#1
print("Задание 1")

def summ(x, y, z):
	print(x + y + z)

a = float(input("Введите число: "))
b = float(input("Введите число: "))
c = float(input("Введите число: "))

summ(a,b,c)

#2
print("Задание 2")

def area(x, y):
	print(x*y*0.5)

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

area(a,b)

#3
print("Задание 3")

def oclock(n):
	minutes = n % 60
	hours = n // 60
	print("Ты ошибся..." if hours > 23 else str(hours) + ":" + str(minutes))

a = int(input("Введите кол-во минут: "))

oclock(a)

#4
print("Задание 4")

def boots(a, b, l, N):
	length = (N - 1) * (a + b) - b + 2 * l
	print(length)

a = int(input("Расстояние между рядами равно: "))
b = int(input("Расстояние между дырочками равно: "))
c = int(input("Дина хвостов шнурка равна: "))
d = int(input("Кол-во дырочек равно: "))

boots(a, b, c, d)

#5
print("Задание 5")

def min_three(x, y, z):
	m = x if x < y else y
	m = m if m < z else z
	print(m)

a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))

min_three(a, b, c)

#6
print("Задание 6")

def chess(a_x, a_y, b_x, b_y):
	if (a_x % 2 + a_y % 2) % 2 == (b_x % 2 + b_y % 2) % 2:
		print("Да")
	else: 
		print("Нет")

a = int(input("Введите число столбца от 1 до 8: "))
b = int(input("Введите число строки от 1 до 8: "))
c = int(input("Введите число столбца от 1 до 8: "))
d = int(input("Введите число строки от 1 до 8: "))

chess(a, b, c, d)

#7
print("Задание 7")

def is_visokos(n):
	if n % 400 == 0:
		print("Да")
	elif n % 100 != 0:
		print("Нет")
	elif n % 4 == 0:
		print("Да")
	else: 
		print("Нет")

a = int(input("Введите год: "))

is_visokos(n)

#8
print("Задание 8")

def there_is_sovpad(x, y, z):
	if x == y and y == z:
		print(3)
	elif x == y or x == z or y == z:
		print(2)
	else:
		print(0)

a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))

there_is_sovpad(a, b, c)

#9
print("Задание 9")

def crack_the_chocolate(m, n, k):
	if (k % n == 0 and k // n < m) or (k % m == 0 and k // m < n):
		print("Yes")
	else: 
		print("No")

a = int(input("Введите число m: "))
b = int(input("Введите число n: "))
c = int(input("Введите число k: "))

crack_the_chocolate(m, n, k)
