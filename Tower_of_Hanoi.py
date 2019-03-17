#!/usr/bin/env python

print("Use the recusion...Implement tower of hanoi.")

def Hanoi(n, x, y, z):
	if n < 1:
		print("The num is Error.Please type again.")
		return -1
	if n == 1:
		print(x, " ==> ", z)
	else:
		Hanoi(n - 1, x, z, y)
		print(x, " ==> ", z)
		Hanoi(n - 1, y, x, z)

num = int(input("Please input the num that you want:"))
result = Hanoi(num, 'A', 'B', 'C')

if result != -1:
	print(result)
