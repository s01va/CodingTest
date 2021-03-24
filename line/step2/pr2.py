PGNAMEMINLEN = 1
PGNAMEMAXLEN = 10

FLAGRULESMINLEN = 1
FLAGRULESMAXLEN = 100

# flagname include '-'
FLAGNAMEMINLEN = 2
FLAGNAMEMAXLEN = 10

CMDMINLEN = 1
CMDMAXLEN = 100

def solution(program, flag_rules, commands):
	# 1 <= commands의 길이 <= 100
	if len(commands) < 1 or len(commands) > 100:
		answer = [False for i in commands]
	else:
		answer = [True for i in commands]

	flagrule_dict = {}
	for flag_rule in flag_rules:
		flag_name, flag_argument_type = flag_rule.split(' ')
		flagrule_dict[flag_name] = flag_argument_type

	for command in commands:
		# 1 <= command의 길이 <= 100
		if len(command) < CMDMINLEN or len(command) > CMDMAXLEN:
			answer[commands.index(command)] = False
			continue
		
		cmdprogram, cmdflag_rules_tmp = command.split(' ', 1)

		# cond 1: cmdprogram
		if len(cmdprogram) < PGNAMEMINLEN or len(cmdprogram) > PGNAMEMAXLEN:
			answer[commands.index(command)] = False
			continue
		if cmdprogram != program:
			answer[commands.index(command)] = False
			continue

		# cond 2: cmdflag_rules
		cmdflag_rules = cmdflag_rules_tmp.split("-")[1:]
		if len(cmdflag_rules) < FLAGRULESMINLEN:
			answer[commands.index(command)] = False
			continue
		
		for cmdflag_rule in cmdflag_rules:
			cmdflag_rule = "-" + cmdflag_rule.strip()

			if len(cmdflag_rule) < FLAGRULESMINLEN or len(cmdflag_rule) > FLAGRULESMAXLEN:
				answer[commands.index(command)] = False
				continue

			cmdflag_name = cmdflag_rule.split(' ', 1)[0]

			if len(cmdflag_name) < FLAGNAMEMINLEN or len(cmdflag_name) > FLAGNAMEMAXLEN:
				answer[commands.index(command)] = False
				continue

			for ch in cmdflag_name:
				if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
					pass
				else:
					answer[commands.index(command)] = False
					continue
			print(command)
			print(flagrule_dict[cmdflag_name])
			if flagrule_dict[cmdflag_name] == "NULL":
				if len(cmdflag_rule[FLAGNAMEMINLEN:]) > 0:
					answer[commands.index(command)] = False
					continue
			else:
				if len(cmdflag_rule[FLAGNAMEMINLEN:]) == 0:
					answer[commands.index(command)] = False
					continue
				else:
					cmdflag_argument = cmdflag_rule.split(' ')[1:]
					if flagrule_dict[cmdflag_name] == "NUMBER":
						if len(cmdflag_argument) > 1:
							answer[commands.index(command)] = False
							continue
						if cmdflag_argument[0].isdigit() == False:
							answer[commands.index(command)] = False
							continue
					elif flagrule_dict[cmdflag_name] == "NUMBERS":
						for iargument in cmdflag_argument:
							if iargument.isdigit() == False:
								print(answer)
								answer[commands.index(command)] = False
								continue
					elif flagrule_dict[cmdflag_name] == "STRING":
						for ch in cmdflag_argument[0]:
							if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
								pass
							else:
								print(answer)
								answer[commands.index(command)] = False
								continue
					elif flagrule_dict[cmdflag_name] == "STRINGS":
						for iargument in cmdflag_argument:
							for ch in iargument:
								if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
									pass
								else:
									answer[commands.index(command)] = False
									continue
	print(answer)
	return answer

program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]
solution(program, flag_rules, commands)