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

			cmdflag_name = cmdflag_rule[:FLAGNAMEMINLEN]

			if len(cmdflag_name) < FLAGNAMEMINLEN or len(cmdflag_name) > FLAGNAMEMAXLEN:
				answer[commands.index(command)] = False
				continue

			if 'a' <= cmdflag_name[1] <= 'z' or 'A' <= cmdflag_name[1] <= 'Z':
				pass
			else:
				answer[commands.index(command)] = False
				continue				
			
			if flagrule_dict[cmdflag_name] == "NULL":
				if len(cmdflag_rule[FLAGNAMEMINLEN:]) > 0:
					answer[commands.index(command)] = False
					continue
			else:
				if len(cmdflag_rule[FLAGNAMEMINLEN:]) == 0:
					answer[commands.index(command)] = False
					continue
				else:
					cmdflag_argument = cmdflag_rule.split(' ')[1]
					if flagrule_dict[cmdflag_name] == "NUMBER":
						if cmdflag_argument.isdigit() == False:
							answer[commands.index(command)] = False
							continue
					elif flagrule_dict[cmdflag_name] == "STRING":
						for ch in cmdflag_argument:
							if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
								pass
							else:
								answer[commands.index(command)] = False
								continue
	return answer

program = "line"
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -s 123 -n HI", "line fun"]
solution(program, flag_rules, commands)