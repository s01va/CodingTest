x, y = input().split()
x = int(x)
y = int(y)

hours = []
minutes = []
for h in range(0, 24):
	hours.append(h)
for m in range(0, 60):
	minutes.append(m)

if (y-45 < 0):
	print(str(hours[x-1]) + " " + str(minutes[y-45]))
else:
	print(str(hours[x]) + " " + str(minutes[y-45]))
