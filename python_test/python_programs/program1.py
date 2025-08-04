f = open('myfile.txt','w')

print("Please enter text(@ at end):\n")

str = None
while(str != '@'):
	str = input()

	if(str != '@'):
		f.write(str+"\n")

f.close()