import sys
import random

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

allgameN = 9
rps_list = [ROCK, PAPER, SCISSORS]
rps_remain_num = {ROCK:3, PAPER:3, SCISSORS:3}
rps_prob = {ROCK:0, PAPER:0, SCISSORS:0}

def main():
	for gameN in range(0, allgameN):
		
		restgameN = allgameN - gameN

		ROCKprob = (rps_remain_num.get(ROCK) / restgameN) * 100
		rps_prob[ROCK] = ROCKprob
		PAPERprob = (rps_remain_num.get(PAPER) / restgameN) * 100
		rps_prob[PAPER] = PAPERprob
		SCISSORSprob = (rps_remain_num.get(SCISSORS) / restgameN) * 100
		rps_prob[SCISSORS] = SCISSORSprob

		max_rpsN = max(rps_remain_num[ROCK], rps_remain_num[PAPER], rps_remain_num[SCISSORS])
		maxwhats = []
		for member in rps_list:
			maxwhat = rps_remain_num.get(member)
			if maxwhat == max_rpsN:
				maxwhats.append(member)

		print("")
		print("+==========+==========+==========+")
		print("| SCISSORS |   ROCK   |   PAPER  |")
		print("+----------+----------+----------+")
		print("|    %d회   |    %d회   |    %d회   | : 남은 횟수" % (rps_remain_num.get(SCISSORS), rps_remain_num.get(ROCK), rps_remain_num.get(PAPER)))
		print("+----------+----------+----------+")
		print("| %6.1f%%  | %6.1f%%  | %6.1f%%  | : 등장 확률" % (SCISSORSprob, ROCKprob, PAPERprob))
		print("+==========+==========+==========+")
		print("|   ROCK   |  PAPER   | SCISSORS | : 이기는 선택지")
		print("+----------+----------+----------+")
		print("")

		bestchoice = ROCK

		if (len(maxwhats) == 3):
			print("  최선의 선택지: Random")
		elif (len(maxwhats) == 2):
			if (whowin(maxwhats[0]) == maxwhats[1]):
				bestchoice = maxwhats[1]
			elif (whowin(maxwhats[1] == maxwhats[0])):
				bestchoice = maxwhats[0]
		elif (len(maxwhats) == 1):
			bestchoice = whowin(maxwhats[0])
		else:
			pass
		
		print("  최선의 선택지: " + bestchoice)

		print("  (이길 확률: %.1f%%)" % rps_prob[wholose(bestchoice)])
		print("  (비길 확률: %.1f%%)" % rps_prob[bestchoice])
		print("  (  질 확률: %.1f%%)" % rps_prob[whowin(bestchoice)])
		
		print("\n")

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
				rps_remain_num[ROCK] = rps_remain_num[ROCK] - 1
				break
			elif (input_rps == str(2)):
				rps_remain_num[PAPER] = rps_remain_num[PAPER] - 1
				break
			elif (input_rps == str(3)):
				rps_remain_num[SCISSORS] = rps_remain_num[SCISSORS] - 1
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