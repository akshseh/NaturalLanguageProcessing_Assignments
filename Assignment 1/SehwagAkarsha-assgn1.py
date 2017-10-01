import re
#input a file
inputfile = open('Testt.txt', 'r')
count = 0
#find the paragraphs
for line in inputfile.read().split('\n\n'):
	if line!='':
		count = count + 1
print("Number of paragraphs:")
print(count)
inputfile.close()

#find the tokens
inputfile = open('Testt.txt', 'r')
countx = 0
tokens = inputfile.read().split()
for tok in tokens:
	if tok != '-':
		countx= countx + 1
print("Number of tokens: ")
print(countx)

tcount = 0
flag = 0
#find the number of lines
for string in tokens:
	
	if flag == 1 and string[0].isupper() == True :
		tcount = tcount + 1
		flag = 0

	if string.endswith('.') or string.endswith('!') or string.endswith('?') :
		flag = 1

	if string.endswith('.') and string[0].isupper == True :
		flag = 0

print("Number of lines: ")
print(tcount)

inputfile.close()