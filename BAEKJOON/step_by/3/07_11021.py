import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N+1):
	inputnum = sys.stdin.readline().rstrip().split()
	print("Case #%s: %s" %(i, int(inputnum[0]) + int(inputnum[1])))
