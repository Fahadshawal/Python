#This Function is Used To clear The Screen
def Clear():
	import os
	os.system('clear')
	return
	
#This Function Will Show The Algorithums
def ShowList():
	Clear()
	print("\v\v\v\t\t       -: Algorithums :-")
	print("\t      -: First Come First Serve ----->  1 :-")
	print("\t      -: Short Job First ------------>  2 :-")
	print("\t      -: Short Remaining Time First ->  3 :-\n")
	return raw_input()
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
		dictlist.append(info)
		num1 = num1+1
	return
#------------------------------------------------------------------------------------------------------------
#function is doing first come first surve
#------------------------------------------------------------------------------------------------------------	
def FCFS(num,dictlist):

	Clear()
	print "FIRST COME FIRST SERVE ALGORITHUM IS RUNNING"
	total = 0
	loop = 0
	inloop = 0
	from operator import itemgetter
	dictlist.sort(key = itemgetter('arrive'))
	while(loop < num):
		if loop == 0:
			total = total + dictlist[loop]['arrive'] + dictlist[loop]['process']
		elif total > dictlist[loop]['arrive']:
			total = total + dictlist[loop]['process']
		else:
			total = dictlist[loop]['arrive']  + dictlist[loop]['process']
			
		print "%s Takes %d sec to complete its processing" % (dictlist[loop]['name'],total)
		loop = loop+1	
	print "FIRST COME FIRST SERVE ALGORITHUM IS ENDS \n "
	
#------------------------------------------------------------------------------------------------------------
#function is doing short job first
#------------------------------------------------------------------------------------------------------------	
def SJF(num,dictlist):
	print "SHORT JOB FIRST SERVE ALGORITHUM IS RUNNING"
	total = 0
	loop = 0
	inloop = 0
	from operator import itemgetter
	dictlist.sort(key = itemgetter('process'))
	while(loop < num):
		if loop == 0:
			total = total + dictlist[loop]['arrive'] + dictlist[loop]['process']
		else:
			total = total + dictlist[loop]['process']
		print "%s Takes %d sec to complete its processing" % (dictlist[loop]['name'],total)
		loop = loop+1
	print "SHORT JOB FIRST SERVE ALGORITHUM IS ENDS \n"

#------------------------------------------------------------------------------------------------------------
#function is doing shortest ramining time first
#------------------------------------------------------------------------------------------------------------	
def SRTF(num,dictlist):
	print "SHORT JOB FIRST SERVE ALGORITHUM IS RUNNING"
	total = 0
	loop = num
	ready = []
	from operator import itemgetter
	dictlist.sort(key = itemgetter('arrive'))
	temp = dictlist[0]
	del dictlist[0]
	total = temp['arrive']
	
	while(loop):
		if(len(dictlist) != 0):
			if(dictlist[0]['arrive'] <= total):
				ready += [dictlist[0]]
				del dictlist[0]
			
		if(len(ready) != 0):
			ready.sort(key = itemgetter('process'))

		if(len(ready) != 0 ):
			if(temp['process'] > ready[0]['process']):
				ready += [temp]
				temp = ready[0]
				del ready[0]
		
		temp['process'] -= 1
		total += 1
		if(temp['process'] == 0):
			print "%s Turn Around Time Is : %d  Waiting Time Is : %d" % (temp['name'],total,total-(temp['arrive']+temp['sum']))
			loop = loop - 1
			if(len(ready) != 0):
				temp = ready[0]
				del ready[0]

	print "SHORT JOB FIRST SERVE ALGORITHUM IS ENDS \n"

	
#-------------------------------------------------------#
#Here Is the Main Progrma Will executed Using Functions #
#-------------------------------------------------------#

#ch = ShowList()
num = GetNumber()

dictlist = []
GetInput(num,dictlist)
FCFS(num,dictlist)
SJF(num,dictlist)
SRTF(num,dictlist)
