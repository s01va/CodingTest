n = input()
n = int(n)

results = []
for i in range(0, n):
	x, y = input().split()
	x = int(x)
	y = int(y)
	results.append(x + y)

for result in results:
	print(str(result))