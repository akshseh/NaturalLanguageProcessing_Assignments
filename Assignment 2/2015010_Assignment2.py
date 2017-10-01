# //Insertion Deletion: 1
# //Substitution cost: 2
def edit_dist(inp1,inp2,arr):
	for i in range(0,len(inp1)+1):
		
		for j in range(0,len(inp2)+1):
		
			if i==0:
				arr[i][j] = j
			elif j==0:
				arr[i][j] = i
			elif inp1[i-1]==inp2[j-1]:
				arr[i][j] = arr[i-1][j-1]
			else:
				arr[i][j] = 1 + min(arr[i][j-1], arr[i-1][j],1+arr[i-1][j-1])
				#j-1 insert i-1 remove i-1 j-1 replace
				#print(arr[i][j]," ",i,j),
	ans = arr[len(inp1)][len(inp2)]
	return ans,arr

inp1 = input()
#print(inp1)
#print(len(inp1))
inp2 = input()
#print(inp2)
#print(len(inp2))
arr = [[0 for x in range(len(inp1)+1)] for y in range(len(inp2)+1)]
temp,arr = edit_dist(inp1,inp2,arr)
print("Edit distance is: ", temp)
print("Alignment:")
newx = []
newy = []
newp = []
	
i = len(inp1)
j = len(inp2)	
while i>0 or j>0:
	m = min(arr[i][j-1],arr[i-1][j-1],arr[i-1][j])
	if arr[i-1][j-1] == m:
		newp.append(0) #Substitution
		i = i-1
		j = j-1
	elif arr[i][j-1] == m:
		newp.append(1)  #Insertion
		j = j-1
	elif arr[i-1][j] == m:
		newp.append(2) #Deletion
		i = i-1
	newx.append(i)
	newy.append(j)

a = len(newy)-1

while a>=0:
	if newp[a]==2:
		#deletion
		print(inp1[newx[a]]," --  *    (d)")
	elif newp[a]==1:
		#insertion
		print("*  -- ",inp2[newy[a]],"   (i)")
	else:
		if(ord(inp2[newy[a]]) == ord(inp1[newx[a]])):
			print(inp1[newx[a]]," -- ",inp2[newy[a]])
		else:
			print(inp1[newx[a]]," -- ",inp2[newy[a]],"   (s)")
	a = a-1
