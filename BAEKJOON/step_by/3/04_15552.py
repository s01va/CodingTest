import sys

T = int(sys.stdin.readline().rstrip())

results = []
for i in range(0, T):
	num = sys.stdin.readline().rstrip().split()
	results.append(str(int(num[0])+int(num[1])))

for result in results:
	print(result)