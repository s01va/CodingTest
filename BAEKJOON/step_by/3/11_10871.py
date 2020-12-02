import sys

A, X = sys.stdin.readline().rstrip().split()
A = int(A)
X = int(X)

arr = [0 for i in range(A)]
arr = sys.stdin.readline().rstrip().split()	
arr = [int(i) for i in arr]

result = []
for i in arr:
	if i < X:
		sys.stdout.write(str(i) + " ")