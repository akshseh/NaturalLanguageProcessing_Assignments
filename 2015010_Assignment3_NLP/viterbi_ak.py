import nltk
from collections import Counter
#replace distinct tags by qtags
filename = 'trainingSet.txt'
file2 = 'testfile.txt'

file = open(filename,'r')
openfile = file.read()

testfile = open(file2,'r')
opentest = testfile.read()

#List of distinct tags
All_tags = []
All_tags.append('ST')
for line in file.readlines():
	if line != ' \n':
		tag = line.split(' ')
		if tag[1] not in All_tags:
			All_tags.append(tag[1])
# transition prob matrix A - moving from i to j 		n*n
# A mat - x --curr y--prev
tg = []
i=0
matrix_A = [[1 for x in range(len(All_tags)+1)] for y in range(len(All_tags)+1)]
for j in range(1,matrix_A.len()):
    matrix_A[0][j] = All_tags[i]
    matrix_A[j][0] = All_tags[i]   
    i = i+1
prev = ''
ind  = ''
for t in file.readlines():
	if t != '\n':
		tg = t.split(' ')
	else:
		tg[1] = 'ST'	
	ind = All_tags.index(tg[1]) + 1
	if prev != '':
		matrix_A[ind][prev] = matrix_A[ind][prev]+1
	prev = ind
sum_mat = []
for j in range(1,len(matrix_A)):
	for i in range(1,len(matrix_A[j])):
		sum_mat[i] = sum_mat[i]+ matrix_A[j][i]
for j in range(1,len(matrix_A)):
	for i in range(1,len(matrix_A[j])):
		matrix_A[j][i] = matrix_A[j][i]/float(sum_mat[i])


# array O obser = drawn from vocab V
O_sentence = []
for line in testfile.read().split('\n\n'):
	# get the line	Obs matrix
	O_sentence = line.split('\n')
	sentence_len = len(O_sentence)
	# Observation likelihood emission prob - B
	B_matrix = [[1 for x in range(sentence_len+1)] for y in range(len(All_tags)+1)]

	# In the given corpus create a dictionary for all the words
	# for all tag 1 find all hello+tag1 * P(tag1)
	# prob of hello from tag1
	dictionary = {}
	for line in file.readlines():
		a = line.split(' ')
		if dictionary.has_key(a[1]):
			dictionary[a[1]].append(a[0])
		else:
			dictionary[a[1]] = []
			dictionary[a[1]].append(a[0])
	#all tag1
	for j in range(1,len(B_matrix)):
		B_matrix[j][0] = All_tags[j-1]
	for j in range(1,len(B_matrix[0])):
		B_matrix[0][j] = O_sentence[j-1]
	

	count = 0
	# traversing the entire matrix
	for j in range(1,len(B_matrix)):
		for i in range(1,len(B_matrix[0])):
			totwords = len(dictionary.get(B_matrix[j][0]))
			count = 0
			for val in dictionary.get(B_matrix[j][0]):
				if B_matrix[0][i].equals(val):
					count=count+1
			B_matrix[j][i] = count/float(totwords)

	
	#viterbi = []
	bckptr = []
	prev_vit = {}
	path = {}
	viterbi = [[1 for x in range(sentence_len+2)] for y in range(len(All_tags))]

	for t in All_tags:
		viterbi[t][0] = matrix_A[t+1][1] * B_matrix[t+1][1]
		bckptr[t][1] = 0

	for w in range(1,O_sentence):
		newpath = {}
		for t in len(All_tags)):
			tmp = 0
			s = 0
			for tg in All_tags:
				tmp = viterbi[tg][w-1] * matrix_A[tg][t] * B_matrix[y][w]
				s = tg
				if(max < tmp):
					tmp = max
					s = tg
			viterbi[t][w] = tmp
			newpath[t] = path[s]+[t]
		path = newpath

	ma = 0
	#TERMINATION
	if len(O_sentence)!=1:
		ma = t
	pr,st = max((viterbi[x][ma],x) for x in All_tags)
	print pr, path[st]
# \\\\\\\\\\\\\\\\\\
# vit = [{}]
#         path = {}     
#         # Initialize base cases (t == 0)
#         for y in self.states:
#             vit[0][y] = self.pi[y] * self.B[y][obs[0]]
#             path[y] = [y]
     		
#         # Run Viterbi for t > 0
#         for t in range(1, len(obs)):
#             vit.append({})
#             newpath = {}     
#             for y in self.states:
#                 (prob, state) = max((vit[t-1][y0] * self.A[y0][y] * self.B[y][obs[t]], y0) for y0 in self.states)
#                 vit[t][y] = prob
#                 newpath[y] = path[state] + [y]     
#             # Don't need to remember the old paths
#             path = newpath
#         n = 0           
#         # if only one element is observed max is sought in the initialization values
#         if len(obs)!=1:
#             n = t
#         (prob, state) = max((vit[n][y], y) for y in self.states)
#         return (prob, path[state])
# # ///////////////////////////////////

f.close()