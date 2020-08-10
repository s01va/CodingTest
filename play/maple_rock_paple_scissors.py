import sys
import random

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

allgameN = 9
rps_list = [ROCK, PAPER, SCISSORS]
rps_dict = {ROCK:3, PAPER:3, SCISSORS:3}
rps_random = []
for i in range(0, 3):
	rps_random.append(ROCK)
	rps_random.append(PAPER)
	rps_random.append(SCISSORS)

def main():
	for gameN in range(0, allgameN):
		restgameN = allgameN - gameN
		ROCKprob = (rps_dict.get(ROCK) / restgameN) * 100
		PAPERprob = (rps_dict.get(PAPER) / restgameN) * 100
		SCISSORSprob = (rps_dict.get(SCISSORS) / restgameN) * 100

		max_rpsN = max(rps_dict[ROCK], rps_dict[PAPER], rps_dict[SCISSORS])
		maxwhats = []
		for member in rps_list:
			maxwhat = rps_dict.get(member)
			if maxwhat == max_rpsN:
				maxwhats.append(member)

		print("")
		print("+==========+==========+==========+")
		print("| SCISSORS |   ROCK   |   PAPER  |")
		print("+----------+----------+----------+")
		print("|    %d회   |    %d회   |    %d회   | : 남은 횟수" % (rps_dict.get(SCISSORS), rps_dict.get(ROCK), rps_dict.get(PAPER)))
		print("+----------+----------+----------+")
		print("| %6.1f%%  | %6.1f%%  | %6.1f%%  | : 등장 확률" % (SCISSORSprob, ROCKprob, PAPERprob))
		print("+==========+==========+==========+")
		print("|   ROCK   |  PAPER   | SCISSORS | : 이기는 선택지")
		print("+----------+----------+----------+")
		print("")

		if (len(maxwhats) == 3):
			print("최선의 선택지: Random")
		elif (len(maxwhats) == 2):
			if (whowin(maxwhats[0]) == maxwhats[1]):
				print("최선의 선택지: " + maxwhats[1])
			elif (whowin(maxwhats[1] == maxwhats[0])):
				print("최선의 선택지: " + maxwhats[0])
		elif (len(maxwhats) == 1):
			print("최선의 선택지: " + whowin(maxwhats[0]))
		else:
			pass
		
		print("")

		while(True):
			print("# 내가 낸 선택지 입력:")
			print("ROCK: 1  PAPER: 2  SCISSORS: 3")
			input_rps = input("> ")
			if (input_rps == str(1)):
				
				break
			elif (input_rps == str(2)):
				
				break
			elif (input_rps == str(3)):
				
				break
			else:
				print("Please input again")

		while(True):
			print("# 실제 나온 선택지 입력:")
			print("ROCK: 1  PAPER: 2  SCISSORS: 3")
			input_rps = input("> ")
			if (input_rps == str(1)):
				rps_dict[ROCK] = rps_dict[ROCK] - 1
				break
			elif (input_rps == str(2)):
				rps_dict[PAPER] = rps_dict[PAPER] - 1
				break
			elif (input_rps == str(3)):
				rps_dict[SCISSORS] = rps_dict[SCISSORS] - 1
				break
			else:
				print("Please input again")



def whowin(rps):
	if rps == ROCK:
		return PAPER
	elif rps == PAPER:
		return SCISSORS
	elif rps == SCISSORS:
		return ROCK
	else:
		return "error"

def wholose(rps):
	if rps == ROCK:
		return SCISSORS
	elif rps == PAPER:
		return ROCK
	elif rps == SCISSORS:
		return PAPER
	else:
		return "error"


if __name__ == "__main__":
	main()
	sys.exit(0)