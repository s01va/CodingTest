x = input()
x = int(x)

if (x % 400 == 0):
	print("1")
elif (x % 100 != 0) and (x % 4 == 0):
	print("1")
else :
	print("0")