import nltk
import sys


def myfunc(all_first,first,output,rule,strr):
	if rule[0] != first:
		output = output+strr
	else:
	 	all_first = all_first+strr
	return all_first,output

def Tostring(rule):
	s = rule[0]+ ' ->'
	for r in rule[1:]:
		s = s+' '+r
	s = s+'\n'
	return s

def convert_longCFG(file):
	i = 1
	all_first = ''
	init_sym = 1
	first = ''
	ruleMap = {}
	single = 0
	singles = []
	output = ''
	with open(file) as filename:
		x = 1
		while x == 1:
			line = filename.readline()
			line = line.strip()
			if line == '':
				break
			if line[0] =='#' or line[0] == '%':
				continue
			else:
				line = line.split('->')
				left = line[0].strip()
				right = line[1:][0].strip().split('|')

				if init_sym == 1:
					first = left
					init_sym = 0
				#singles at last
				for element in right:
					single = 0
					rule = [left]+ element.split()

					if rule[1][0] != '"' and len(rule) < 3:
						single = 1
						singles.append(rule)

					if len(rule) >= 3:
						#find terminals
						index = []
						terminals = []
						k = 0
						for x in rule:
							k= k+1
							if x[0] == '"':
								index.append(k-1)
								terminals.append(x)
						
						if len(terminals) >= 1:
							#replaces terminals with new non-terminals
							#add new rules
							strr = ''
							for j in range(0,len(index)):
								#replace terminals
								kk=index[j]
								nNode = 'Z' + str(i)
								rule[kk] = nNode
								strr += Tostring([nNode] + [terminals[j]])

								# rule = [nNode] + [terminals[j]]
								# s = rule[0] + ' ->'
								# for r in rule[1:]:
								# 	s += ' ' + r
								# s += '\n'
							i = i+1
							# if rule[0] != first:
							# 	output = output+strr
							# else:
							# 	all_first = all_first+strr
							all_first, output = myfunc(all_first,first,output,rule,strr)

						#handle long waale grammar
						while len(rule) >= 4:
							nNode = 'Z' + str(i)
							strr = Tostring([nNode] + rule[1:3])
							rule = [rule[0]] + [nNode] + rule[3:]
							i = i+1
							#if rule[0] != first:
							# 	output = output+strr
							# else:
							# 	all_first = all_first+strr
							all_first, output = myfunc(all_first,first,output,rule,strr)
					
					#add rule
					if rule[0] not in ruleMap:
						ruleMap[rule[0]] = []
					ruleMap[rule[0]].append(rule[1:])

					if single == 0:
						xyz = Tostring(rule)			
						all_first, output = myfunc(all_first,first,output,rule,xyz)
	#///////////////////////
	#LETS HANDLE SINGLES

	output2 = ''
	all_first2 = ''
	while len(singles) >= 1:
		rule = singles.pop()
		oppa = rule[1]
		if oppa in ruleMap:
			for xyz in ruleMap[oppa]:
				nRule = [rule[0]] + xyz

				if len(nRule) < 3 and nRule[1][0] != '"':
					singles.append(nRule)
				else:
					xz = Tostring(nRule)			
					all_first2, output2 = myfunc(all_first2,first,output2,nRule,xz)
				

				#add rule
				xx = nRule[0]
				if xx not in ruleMap:
					ruleMap[xx] = []
				ruleMap[xx].append(nRule[1:])

	all_first = all_first + all_first2
	output = output + output2

	return all_first,output



print("CFG_to_CNF [.cfg file] [output file]")
CFgrammar = sys.argv[1]
#CFgrammar = nltk.data.load("large_grammars/atis.cfg")

#nltk.data.show_cfg("grammars/large_grammars/atis.cfg")
outputfile = sys.argv[2]
print(outputfile)
#print(CFgrammar)
all_first, output = convert_longCFG(CFgrammar)

print(all_first)
print(output)
with open(outputfile,'w') as filename:
	filename.write(all_first)
	filename.write(output)



