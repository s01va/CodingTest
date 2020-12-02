import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N+1):
	for j in range(N, i, -1):
		sys.stdout.write(" ")
	for k in range(1, i+1):
		sys.stdout.write("*")
	sys.stdout.write("\n")
