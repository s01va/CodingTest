import sys

while(True):
	A, B = sys.stdin.readline().rstrip().split()
	if (int(A) == 0) and (int(B) == 0):
		break
	sys.stdout.write(str(int(A) + int(B)) + "\n")