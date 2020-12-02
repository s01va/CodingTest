import sys

N = int(sys.stdin.readline().rstrip())
cycle = 1

if N < 10:
	N = N * 10

tmpN = N
while(True):
	a = tmpN // 10
	b = tmpN % 10
	tmpN = 10 * b + ((a + b) % 10)
	if (tmpN != N):
		cycle = cycle + 1
	else:
		break
sys.stdout.write(str(cycle))
