#!/usr/bin/python
# encode : utf-8
import serial
from datetime import datetime
import time
import urllib
import pdb

port=serial.Serial(port='/dev/ttyAMA0',baudrate=9600, timeout=1.0)
eof = "\xff\xff\xff"
#API for temp
temp = ""
cmd1 = "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=BHYO26QLWEDGG7WI"
#API for Weather conditions
cond = ""
cmd2 = "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=VA2YN7ZD2WYJBCFF" 
#API for dust
dust = ""
cmd3 = "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=07W76PN9B4DG848U"
#API for mdust
mdust = ""
cmd4 = "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=EV04SJAXT8EJK2OC"
#alt = 'page0.Date.txt="'+tm+'"'+eof
fullTemp = ""
fullCond = ""
dimCmd = "dim=0"
undimCmd = "dim=100"
IsDim = 0
hour24 = 0
Page = 0 
pic = 0
Opic = 0
WDesc = ""
debugON = 1

#get temp Sub
def GetTemp():
	global temp
	response = urllib.urlopen(cmd1)
	temp = response.read()
	temp = temp[temp.find('>')+1:temp.find('<',2)]
	
#get conditions Sub
def GetCond():
	global cond
	global WDesc
	response = urllib.urlopen(cmd2)
	cond = response.read()
	cond = cond[cond.find('>')+1:cond.find('<',2)]
	WDesc = cond
	
def GetDust():
	global dust
	response = urllib.urlopen(cmd3)
	dust = response.read()
	dust = dust[dust.find('m">',3)+3:dust.find('</s')-7]
	
def GetMDust():
	global mdust
	response = urllib.urlopen(cmd4)
	mdust = response.read()
	mdust = mdust[mdust.find('m">',3)+3:mdust.find('</s')-7]
	
#Get weather and conditions at startup ratrher thanm wait till mins = 00
GetTemp()
GetCond()
GetDust()
GetMDust()
#Units()

while True: 
#formatting date for screen
	x = datetime.now()
	weekday = x.strftime("%a")
	month = x.strftime("%B")
	day = x.strftime("%d")
	year = x.strftime("%Y")
	yearN = x.strftime("%y")
	monthN = x.strftime("%m")
	fullDate = (weekday + ", " + month + " " + day + " " + year) 
	fullDate1 = 'page0.Date.txt="'+fullDate+'"'+eof
	fullDateP1 = 'page1.Date.txt="'+fullDate+'"'+eof
#formatting time for screen
	hour = x.strftime("%I")
	min = x.strftime("%M")
	sec = x.strftime("%S")
	AmPm = x.strftime("%p")
	fullTime = (hour+":"+min+":"+sec+" "+AmPm)
	fullTime1 = 'page0.Time.txt="'+fullTime+'"'+eof
	fullTimeP1 = 'page1.LTime.txt="'+hour+":"+min+":"+sec+'"'+eof
#formatting time for easy time comparison (24hour time)
	hour24 = x.strftime("%H")
#formatting for screen
	fullTemp = 'page0.Temp.txt="'+temp+'"'+eof
	fullCond = 'page0.Stat.txt="'+cond+'"'+eof
	fullDust = 'page0.Dst.txt="'+dust+'"'+eof
	fullMDust = 'page0.mDst.txt="'+mdust+'"'+eof

	#check once an hour for updated temp & conditions
	if ((str(min) == "00") and (str(sec) == "00") and (int(hour24) >= 6) and (int(hour24) <= 21)): 
		GetCond()
	if ((str(min) == "01") and (str(sec) == "00") and (int(hour24) >= 6) and (int(hour24) <= 21)):  
		GetTemp()
	if ((str(min) == "02") and (str(sec) == "00") and (int(hour24) >= 6) and (int(hour24) <= 21)):  
		GetDust()
	if ((str(min) == "03") and (str(sec) == "00") and (int(hour24) >= 6) and (int(hour24) <= 21)):  
		GetMDust()

	#sending info to screen
	if debugON == 1:
		print("************")
		print(fullTime)
		print("temp = " + temp)
		print("cond = " + cond)
		print("WDesc = " + WDesc)
		print("dust = " + dust)
		print("mdust = " + mdust)
		print("hour24 = " + hour24)
		print("integer hour24 = " + str(int(hour24)))
		print("page = " + str(Page))
		print("IsDim = " + str(IsDim))
		print("pic = " + str(pic))
		print("Opic = " + str(Opic))
	port.write(fullDate1)
	port.write(fullTime1)
	port.write(fullTemp)
	port.write(fullCond)
	port.write(fullDust)
	port.write(fullMDust)
	port.write(fullTimeP1)

	# Change display by Weather Condition
	if ((WDesc == "Cloudy") or (WDesc == "Partly Cloudy") or (WDesc == "Mostly Cloudy") or (WDesc == "Overcast")):
		pic = 1
		if (Opic == pic):
			pass#//do nothing pic shouldnt change
		else:
			port.write("p0.pic=1" + eof)
			port.write("Date.picc=1" + eof)
			port.write("Time.picc=1" + eof)
			port.write("Temp.picc=1" + eof)
			port.write("Stat.picc=1" + eof)
			port.write("Dst.picc=1" + eof)
			port.write("mDst.picc=1" + eof)
			port.write("C.picc=1" + eof)
			port.write("um1.picc=1" + eof)
			port.write("um2.picc=1" + eof)
			port.write("Date.pco=65535" + eof)
			port.write("Time.pco=65535" + eof)
			port.write("Temp.pco=65535" + eof)
			port.write("Stat.pco=65535" + eof)
			port.write("Dst.pco=65535" + eof)
			port.write("mDst.pco=65535" + eof)
			port.write("C.pco=65535" + eof)
			port.write("um1.pco=65535" + eof)
			port.write("um2.pco=65535" + eof)
			pic = 1
			Opic = pic

	if ((WDesc == "Sunny") or (WDesc == "Clear") or (WDesc == "Fair")):
		pic = 0
		if (Opic == pic):
			pass#//do nothing pic shouldnt change
		else:
			port.write("p0.pic=0" + eof)
			port.write("Date.picc=0" + eof)
			port.write("Time.picc=0" + eof)
			port.write("Temp.picc=0" + eof)
			port.write("Stat.picc=0" + eof)
			port.write("Dst.picc=0" + eof)
			port.write("mDst.picc=0" + eof)
			port.write("C.picc=0" + eof)
			port.write("um1.picc=0" + eof)
			port.write("um2.picc=0" + eof)
			port.write("Date.pco=2093" + eof)
			port.write("Time.pco=2093" + eof)
			port.write("Temp.pco=2093" + eof)
			port.write("Stat.pco=2093" + eof)
			port.write("Dst.pco=2093" + eof)
			port.write("mDst.pco=2093" + eof)
			port.write("C.pco=2093" + eof)
			port.write("um1.pco=2093" + eof)
			port.write("um2.pco=2093" + eof)
			pic = 0
			Opic = pic

	if ((WDesc == "Snow")):
		pic = 4
		if (Opic == pic):
			pass#//do nothing pic shouldnt change
		else:
			port.write("p0.pic=4" + eof)
			port.write("Date.picc=4" + eof)
			port.write("Time.picc=4" + eof)
			port.write("Temp.picc=4" + eof)
			port.write("Stat.picc=4" + eof)
			port.write("Dst.picc=4" + eof)
			port.write("mDst.picc=4" + eof)
			port.write("C.picc=4" + eof)
			port.write("um1.picc=4" + eof)
			port.write("um2.picc=4" + eof)
			port.write("Date.pco=2093" + eof)
			port.write("Time.pco=2093" + eof)
			port.write("Temp.pco=2093" + eof)
			port.write("Stat.pco=2093" + eof)
			port.write("Dst.pco=2093" + eof)
			port.write("mDst.pco=2093" + eof)
			port.write("C.pco=2093" + eof)
			port.write("um1.pco=2093" + eof)
			port.write("um2.pco=2093" + eof)
			pic = 4
			Opic = pic

	if ((WDesc == "Rain")):
		pic = 2
		if (Opic == pic):
			pass#//do nothing pic shouldnt change
		else:
			port.write("p0.pic=2" + eof)
			port.write("Date.picc=2" + eof)
			port.write("Time.picc=2" + eof)
			port.write("Temp.picc=2" + eof)
			port.write("Stat.picc=2" + eof)
			port.write("Dst.picc=2" + eof)
			port.write("mDst.picc=2" + eof)
			port.write("C.picc=2" + eof)
			port.write("um1.picc=2" + eof)
			port.write("um2.picc=2" + eof)
			port.write("Date.pco=65535" + eof)
			port.write("Time.pco=65535" + eof)
			port.write("Temp.pco=65535" + eof)
			port.write("Stat.pco=65535" + eof)
			port.write("Dst.pco=65535" + eof)
			port.write("mDst.pco=65535" + eof)
			port.write("C.pco=65535" + eof)
			port.write("um1.pco=65535" + eof)
			port.write("um2.pco=65535" + eof)
			pic = 2
			Opic = pic

	if ((WDesc == "Fog")):
		pic = 3
		if (Opic == pic):
			pass#//do nothing pic shouldnt change
		else:
			port.write("p0.pic=3" + eof)
			port.write("Date.picc=3" + eof)
			port.write("Time.picc=3" + eof)
			port.write("Temp.picc=3" + eof)
			port.write("Stat.picc=3" + eof)
			port.write("Dst.picc=3" + eof)
			port.write("mDst.picc=3" + eof)
			port.write("C.picc=3" + eof)
			port.write("um1.picc=3" + eof)
			port.write("um2.picc=3" + eof)
			port.write("Date.pco=0" + eof)
			port.write("Time.pco=0" + eof)
			port.write("Temp.pco=0" + eof)
			port.write("Stat.pco=0" + eof)
			port.write("Dst.pco=0" + eof)
			port.write("mDst.pco=0" + eof)
			port.write("C.pco=0" + eof)
			port.write("um1.pco=0" + eof)
			port.write("um2.pco=0" + eof)
			pic = 3
			Opic = pic

	if ((WDesc != "Clear" and WDesc != "Overcast" and WDesc != "Cloudy" and WDesc != "Mostly Cloudy" and WDesc != "Fog" and WDesc != "Rain" and WDesc != "Sunny" and WDesc != "Snow" and WDesc != "Partly Cloudy" and WDesc != "Fair")):
		pic = 5
		if (Opic == pic):
			pass#//do nothing pic shouldnt change
		else:
			port.write("p0.pic=5" + eof)
			port.write("Date.picc=5" + eof)
			port.write("Time.picc=5" + eof)
			port.write("Temp.picc=5" + eof)
			port.write("Stat.picc=5" + eof)
			port.write("Dst.picc=5" + eof)
			port.write("mDst.picc=5" + eof)
			port.write("C.picc=5" + eof)
			port.write("um1.picc=5" + eof)
			port.write("um2.picc=5" + eof)
			port.write("Date.pco=65535" + eof)
			port.write("Time.pco=65535" + eof)
			port.write("Temp.pco=65535" + eof)
			port.write("Stat.pco=65535" + eof)
			port.write("Dst.pco=65535" + eof)
			port.write("mDst.pco=65535" + eof)
			port.write("C.pco=65535" + eof)
			port.write("um1.pco=65535" + eof)
			port.write("um2.pco=65535" + eof)
			pic = 5
			Opic = pic
	#endregion
