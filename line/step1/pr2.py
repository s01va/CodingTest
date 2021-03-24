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


"""
문제 설명
어떤 메신저 회사에서는 해킹으로부터 고객들을 보호하기 위해, 신규 아이디의 password가 다음 규칙을 만족하도록 강제하고 있습니다.

8 ≤ password 길이 ≤ 15
password는 아래 4 종류의 문자 그룹을 제외한, 다른 어떤 문자도 포함해서는 안됩니다.
[1] 알파벳 대문자(A~Z)
[2] 알파벳 소문자(a~z)
[3] 숫자(0~9)
[4] 특수문자(~!@#$%^&*)
password는 (2.)에서 명시된 4 종류의 문자 그룹 중에서 3 종류 이상을 포함해야 합니다.
password에 어떤 문자라도 같은 문자가 4개 이상 연속될 수 없습니다.
password에 어떤 문자라도 같은 문자가 5개 이상 포함될 수 없습니다.
고객들이 password로 사용하기 위해 입력한 문자열 inp_str가 매개변수로 주어집니다. 이때, 위에서 나열한 규칙들 중 위배되는 규칙들의 번호를 배열에 담아 오름차순 정렬하여 return 하도록 solution 함수를 완성해주세요. 만약 위배된 규칙이 하나도 없다면, 0을 담아서 return 합니다.

제한사항
1 ≤ inp_str의 길이 ≤ 1,000,000
inp_str는 알파벳 대문자(A~Z), 알파벳 소문자(a~z), 숫자(0~9), 특수문자(~!@#$%^&*()-_=+)의 조합으로 구성되는 문자열입니다.
password로 허용되지 않는 특수문자(()-_=+)가 inp_str에는 나타날 수 있습니다.
입출력 예
inp_str	result
"AaTa+!12-3"	[2]
"aaaaZZZZ)"	[2, 3, 4]
"CaCbCgCdC888834A"	[1, 4, 5]
"UUUUU"	[1, 3, 4, 5]
"ZzZz9Z824"	[0]
입출력 예 설명
입출력 예 #1

"AaTa+!12-3"

허용되지 않는 특수문자(+, -)가 포함되어 있습니다.
2번 규칙에 위배됩니다.
입출력 예 #2

"aaaaZZZZ)"

허용되지 않는 특수문자())가 포함되어 있습니다.

2번 규칙에 위배됩니다.
4 종류의 문자 그룹 중에서 3종류 이상이 포함되어 있지 않습니다.

3번 규칙에 위배됩니다.
같은 문자가 4개 이상 연속됩니다.(a, Z)

4번 규칙에 위배됩니다.
입출력 예 #3

"CaCbCgCdC888834A"

길이가 15자를 초과합니다.

1번 규칙에 위배됩니다.
같은 문자가 4개 이상 연속됩니다.(8)

4번 규칙에 위배됩니다.
같은 문자가 5개 이상 포함되어 있습니다.(C)

5번 규칙에 위배됩니다.
입출력 예 #4

"UUUUU"

1,3,4,5번 규칙에 위배됩니다.
입출력 예 #5

"ZzZz9Z824"

위배되는 규칙이 없습니다.
"""