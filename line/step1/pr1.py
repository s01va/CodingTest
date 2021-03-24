def solution(table, languages, preference):
	maxscore = ["", 0]
	for row in table:
		tmp = row.split(' ')
		job = tmp[0]
		langscore = {lang:6-tmp.index(lang) for lang in tmp[1:]}
		score = 0
		for i in range(len(languages)):
			#print(languages[i])
			if langscore.get(languages[i]):
				score += langscore[languages[i]] * preference[i]
		if score >= maxscore[1]:
			maxscore[0] = job
			maxscore[1] = score
	answer = maxscore[0]
	return answer

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
print(solution(table, languages, preference))


# ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
