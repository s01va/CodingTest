import sys
import random

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

allgameN = 9
rps_list = [ROCK, PAPER, SCISSORS]
rps_remain_num = {ROCK:3, PAPER:3, SCISSORS:3}
rps_prob = {ROCK:0, PAPER:0, SCISSORS:0}
rps_random = []
rps_record = {"win":0, "draw":0, "lose":0}

def main():
	f_record = open("RecordData.dat", 'b+')
	print("입력모드: 1 / 게임모드: 2")
	while(True):
		input_mode = input("  > ")
		if (input_mode == "1"):
			break
		elif (input_mode == "2"):
			for i in range(0, 3):
				rps_random.append(ROCK)
				rps_random.append(PAPER)
				rps_random.append(SCISSORS)
			break
		else:
			print("Please input again")

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

		print("\n")
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
			bestchoice = random.choice([ROCK, PAPER, SCISSORS])
		elif (len(maxwhats) == 2):
			if (whowin(maxwhats[0]) == maxwhats[1]):
				bestchoice = maxwhats[1]
			elif (whowin(maxwhats[1]) == maxwhats[0]):
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
			input_rps_choice= input("  > ")
			if (input_rps_choice == str(1)):
				input_rps = ROCK
				break
			elif (input_rps_choice == str(2)):
				input_rps = PAPER
				break
			elif (input_rps_choice == str(3)):
				input_rps = SCISSORS
				break
			else:
				print("Please input again")

		if input_mode == "1":
			while(True):
				print("# 실제 나온 선택지 입력:")
				print("ROCK: 1  PAPER: 2  SCISSORS: 3")
				compare_rps = input("  > ")
				if (compare_rps == str(1)):
					rps_remain_num[ROCK] -= 1
					break
				elif (compare_rps == str(2)):
					rps_remain_num[PAPER] -= 1
					break
				elif (compare_rps == str(3)):
					rps_remain_num[SCISSORS] -= 1
					break
				else:
					print("Please input again")

		if input_mode == "2":
			compare_rps = random.choice(rps_random)
			rps_random.remove(compare_rps)
			rps_remain_num[compare_rps] = rps_remain_num[compare_rps] - 1
			print("# 프로그램의 선택: " + compare_rps)

		######### 전적 구현
		if (input_rps == whowin(compare_rps)):
			rps_record["win"] += 1
		elif (input_rps == wholose(compare_rps)):
			rps_record["lose"] += 1
		else:
			rps_record["draw"] += 1

		print("현재 전적: " + str(rps_record["win"]) + "승 " + str(rps_record["lose"]) + "패 " + str(rps_record["draw"]) + "무")

	print("\n이번 판 전적: " + str(rps_record["win"]) + "승 " + str(rps_record["lose"]) + "패 " + str(rps_record["draw"]) + "무")
	

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