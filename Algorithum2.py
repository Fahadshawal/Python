#This Function is Used To clear The Screen
def Clear():
	import os
	os.system('clear')
	return
	
#This function will get the number of jobs for calculation
def GetNumber():
	Clear()
	print("\v\v\v\t\tHow Many Number Of Job(s) You Want to Enter : ")
	return input()
	
#This function will take input from the user to the dictionary list
def GetInput(num,dictlist):
	Clear()
	num1 = 0
	loop = 0

	while(num1 < num):
		info = {}
		info['name']=raw_input ("Input Name : ")
		info['arrive']=input ("Input A.Time : ")
		info['process']=input ("Input P.Time : ")
		info['brust'] = 0
		info['wait'] = 0
		dictlist.append(info)
		num1 = num1+1
	return
	
#------------------------------------------------------------------------------------------------------------
#function is doing Round Robin time first
#------------------------------------------------------------------------------------------------------------	
def RR(num,dictlist,Slice,IO):
	Clear()
	print "SHORT JOB FIRST SERVE ALGORITHUM IS RUNNING"
	ready = []
	wait = []
	loop = num
	total = 0
	temp = None
	from operator import itemgetter
	wait.sort(key = itemgetter('wait'))	
	while(loop):

		if(len(dictlist) != 0):
			if(dictlist[0]['arrive'] <= total):
				ready += [dictlist[0]]
				del dictlist[0]
		
		if(len(ready) != 0):
			if(temp == None):
				temp = ready[0]
				temp['brust'] = Slice
				del ready[0]
		
		if(temp != None):
			total  += 1
			temp['brust'] -= 1
			temp['process'] -= 1
			
			if(temp['process'] == 0):
				print "%s Turn Around Time is : %d And its Waiting time is : %d" % (temp['name'],total,total-(temp['arrive']+temp['sum']))
				loop -= 1
				if(len(ready) != 0):
					temp = ready[0]
					temp['brust'] = Slice
				else:
					temp = None
			elif(temp['brust'] == 0):
				temp['wait'] = total + IO
				wait += [temp]
				temp = None
		else:
			total += 1
		
		if(len(wait) != 0):
			wait.sort(key = itemgetter('wait'))
			if(wait[0]['wait'] <= total):
				ready += [wait[0]]
				del wait[0]
	

	print "SHORT JOB FIRST SERVE ALGORITHUM IS ENDS \n"

	
#-------------------------------------------------------#
#Here Is the Main Progrma Will executed Using Functions #
#-------------------------------------------------------#
num = GetNumber()

dictlist = []
GetInput(num,dictlist)
SLICE = input("Input The Time Slice : ")
IO = input("Input The I/O Brust Time : ")

RR(num,dictlist,SLICE,IO)
