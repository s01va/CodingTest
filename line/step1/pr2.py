def solution(inp_str):
	violation = []
	# cond 1
	if len(inp_str) < 8 or len(inp_str) > 15:
		violation.append(1)

	meetcond3 = 0
	# cond 2
	tmpstr = inp_str
	for lc in range(ord('A'), ord('Z')+1):
		if chr(lc) in tmpstr:
			tmpstr = tmpstr.replace(chr(lc), '')
			meetcond3 += 1
	for lc in range(ord('a'), ord('z')+1):
		if chr(lc) in tmpstr:
			tmpstr = tmpstr.replace(chr(lc), '')
			meetcond3 += 1
	for lc in range(ord('0'), ord('9')+1):
		if chr(lc) in tmpstr:
			tmpstr = tmpstr.replace(chr(lc), '')
			meetcond3 += 1
	spcstr = "~!@#$%^&*"
	for spc in spcstr:
		if spc in tmpstr:
			tmpstr = tmpstr.replace(spc, '')
			meetcond3 += 1
	if len(tmpstr) > 0:
		violation.append(2)

	# cond 3
	if meetcond3 < 3:
		violation.append(3)

	# cond 4
	ch0 = inp_str[0]
	strflag = 1
	for ch in inp_str[1:]:
		if strflag >= 4:
			violation.append(4)
			break
		else:
			if ch == ch0:
				strflag += 1
			else:
				ch0 = ch

	# cond 5
	setinpstr = set(inp_str)
	for ch in setinpstr:
		if inp_str.count(ch) >= 5:
			violation.append(5)
			break
	
	if len(violation) == 0:
		violation.append(0)

	return violation

solution("UUUUU")
