import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N+1):
	inputnum = sys.stdin.readline().rstrip().split()
	result = str(int(inputnum[0]) + int(inputnum[1]))
	print("Case #%s: %s + %s = %s" %(i, inputnum[0], inputnum[1], result))
