def solution(s):
	answer = 0

	"""
	for striplen in range(1, len(s)-1):
		answer1 = ""
		tmpString = s[0:striplen]
		tmpNum = striplen
		idx = striplen
		for ch in s[striplen:]:
			if ch == tmpString:
				tmpNum = tmpNum + 1
			else:
				answer1 = answer1 + str(tmpNum) + tmpString
				tmpString = ch
				tmpNum = 1
			if idx == (len(s) - 1):
				answer1 = answer1 + str(tmpNum) + tmpString
			idx = idx + 1
		print(answer1)
	"""
	
	# Case 1: 1 length
	answer1 = ""
	tmpString = s[0]
	tmpNum = 1
	idx = 1
	for ch in s[1:]:
		if ch == tmpString:
			tmpNum = tmpNum + 1
		else:
			answer1 = answer1 + str(tmpNum) + tmpString
			tmpString = ch
			tmpNum = 1
		if idx == (len(s) - 1):
			answer1 = answer1 + str(tmpNum) + tmpString
		idx = idx + 1
	print(answer1)
	
	return answer


if __name__ == '__main__':
	s = "aabbaccc"
	solution(s)