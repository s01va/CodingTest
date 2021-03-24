def solution(enter, leave):
	answer = [0 for i in enter]
	room = []
	for entmem in enter:
		room.append(entmem)
		if len(room) > 1:
			for roommem in room:
				if answer[roommem-1] == 0:
					answer[roommem-1] += len(room) - 1
				else:
					answer[roommem-1] += 1
		lvidx = 0
		while leave[lvidx] in room:
			room.remove(leave[lvidx])
			lvidx += 1
	return answer

solution([1,3,2],[1,2,3])