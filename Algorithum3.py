#-----------------------------------------------------------------------------------------------------------
#This Function is Used To clear The Screen
#-----------------------------------------------------------------------------------------------------------
def Clear():
	import os
	os.system('clear')
	return

#------------------------------------------------------------------------------------------------------------
#This function will get the number of jobs for calculation
#------------------------------------------------------------------------------------------------------------
def GetNumber():
	Clear()
	print("\v\v\v\t\tHow Many Number Of Job(s) You Want to Enter : ")
	return input()
	
#------------------------------------------------------------------------------------------------------------
#This function will take input from the user to the dictionary list
#------------------------------------------------------------------------------------------------------------
def GetInput(num,dictlist):
	Clear()
	loop = num

	while(loop):
		info = {}
		info['name']=raw_input ("Input Name : ")
		info['arrive']=input ("Input A.Time : ")
		info['process']=input ("Input P.Time : ")
		info['sum'] = info['process']
		info['slice'] = 0
		info['brust'] = 0
		info['wait'] = 0
		dictlist.append(info)
		loop -= 1
	return



#------------------------------------------------------------------------------------------------------------
#function is doing Vurtual Round Robin 
#------------------------------------------------------------------------------------------------------------	
def VRR(num,dictlist,Slice):
	Clear()
	print "SHORT JOB FIRST SERVE ALGORITHUM IS RUNNING"
	ready = []
	wait = []
	suspend = []
	loop = num
	total = 0
	temp = None
	from operator import itemgetter
	dictlist.sort(key = itemgetter('arrive'))	
	while(loop):

		if(len(dictlist) != 0):
			if(dictlist[0]['arrive'] <= total):
				ready += [dictlist[0]]
				del dictlist[0]
		
		if(len(suspend) != 0):
			if(temp == None):
				suspend.sort(key = itemgetter('wait'))
				if(suspend[0]['wait'] <= total):
					temp = suspend[0]
					del suspend[0]
		
		elif(len(ready) != 0):
			if(temp == None):
				temp = ready[0]
				del ready[0]
				temp['slice'] = Slice
				temp['brust'] = input("Input Brust Time For Process %s: " % (temp['name']))
				temp['wait']  = input("Input IO wait Time For Process %s: " % (temp['name']))
		
		if(temp != None):
			total += 1
			temp['slice'] -= 1
			temp['brust'] -= 1
			temp['process'] -= 1
			
			if(temp['process'] == 0):
				print "%s Turn Around Time is : %d And its Waiting time is : %d" % (temp['name'],total-temp['arrive'],total-(temp['arrive']+temp['sum']))
				loop -= 1
				temp = None
			elif(temp['slice'] == 0):
				ready += [temp]
				temp = None
			elif(temp['brust'] == 0):
				wait += [temp]
				temp = None
		else:
			total += 1
				
		
		if(len(wait) != 0):
			wait.sort(key = itemgetter('wait'))
			if(wait[0]['wait'] <= total):
				suspend += [wait[0]]
				del wait[0]
	

	print "SHORT JOB FIRST SERVE ALGORITHUM IS ENDS \n"

	
#-------------------------------------------------------#
#Here Is the Main Progrma Will executed Using Functions #
#-------------------------------------------------------#
num = GetNumber()
dictlist = []
GetInput(num,dictlist)
SLICE = input("Input The Time Slice : ")
VRR(num,dictlist,SLICE)
