#!/usr/bin/python
import serial
from datetime import datetime
import time
import urllib
import pdb
from urllib import request
from bs4 import BeautifulSoup

port=serial.Serial(port='/dev/ttyAMA0',baudrate=9600, timeout=1.0)
eof = "\xff\xff\xff"
fullTemp = ""
fullCond = ""
fullDust = ""
fullmDust = ""
dimCmd = "dim=0"
undimCmd = "dim=100"
IsDim = 0
hour24 = 0
#holiday = 0
Page = 0 #page0 is the norm and page 1 is all black with large #'s for easy reading in the AM
pic = 0
Opic = 0
#novD = ""
#novD3 = ""
WDesc = ""
debugON = 1
#Leap = ""
#yc = ""

t = request.urlopen("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=6WM696GI9AM4L7VV")
soup_t = BeautifulSoup(t, "html.parser")
for t_data in soup_t.select('span'):
    temp = t_data.string

s = request.urlopen("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=KNRNAD7LPGJXV55H")
soup_s = BeautifulSoup(s, "html.parser")
for s_data in soup_s.select('strong'):
    status = s_data.string

d = request.urlopen("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=07W76PN9B4DG848U")
soup_d = BeautifulSoup(d, "html.parser")
for d_data in soup_d.select('dd'):
    dust = int(d_data.span.string[:-3])

md = request.urlopen("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=EV04SJAXT8EJK2OC")
soup_md = BeautifulSoup(md, "html.parser")

for md_data in soup_md.select('dd'):
    mdust = int(md_data.span.string[:-3])

def GetTemp():
	global temp
	temp = temp
def GetCond():
	global status
	global WDesc
	WDesc = status
def GetDust():
    global dust
    dust = dust
def GetMDust():
    global mdust
    mdust = mdust

port.write("page 0" + eof)
port.write(undimCmd + eof)
port.write("p0.pic=0" + eof)
GetTemp()
GetCond()

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
	hour24 = x.strftime("%H")#17 24hour time
    #formatting temp for screen
	fullTemp = 'page0.Temp.txt="'+temp+'"'+eof
	fullCond = 'page0.Status.txt="'+status+'"'+eof
    #formatting dust for screen
    fullDust = 'page0.Dust.txt="'+str(dust)+'"'+eof
    fullmDust = 'page0.mDust.txt="'+str(mdust)+'"'+eof

	#check once an hour for updated temp & conditions
	if ((str(min) == "00") and (str(sec) == "00") and (int(hour24) >= 6) and (int(hour24) <= 21)): 
		GetCond()
	if ((str(min) == "01") and (str(sec) == "00") and (int(hour24) >= 6) and (int(hour24) <= 21)):  
		GetTemp()

	#switch to screen#1 when the hour = 5 and back to screen 0 at all other times
	if ((int(hour24) == 5) and (Page == 0)):
			port.write("page 1" + eof)
			Page = 1
			pic = 18
			Opic = 18
			port.write("p1.pic=18" + eof)
			port.write("LTime.picc=18" + eof)
			port.write("LTime.pco=65535" + eof)
			port.write(fullTimeP1)
    elif ((int(hour24) != 5) and (Page == 1)):
			port.write("page 0" + eof)
			Page = 0
			port.write(fullTemp)
			port.write(fullCond)
			port.write(fullDate1)
			port.write(fullTime1)

	#sending info to screen
	if debugON == 1:
		print("************")
		print(fullTime)
		print("temp = " + temp)
		print("cond = " + cond)
		print("WDesc = " + WDesc)
		print("hour24 = " + hour24)
		print("integer hour24 = " + str(int(hour24)))
		print("page = " + str(Page))
		print("IsDim = " + str(IsDim))
		print("pic = " + str(pic))
		print("Opic = " + str(Opic))
		#print("Holiday = " + str(holiday))
		#print("yc = " + str(yc))
		#print("Leap = " + str(Leap))
		#print("NovD = " + str(novD))
		#print("YearN = " + yearN)
		#print("Thanksgiving date = 11/" + str(novD3) + "/" + yearN)
		#print("Nov 1st is on the " + str(novD) + " day of the week")

	port.write(fullDate1)
	port.write(fullTime1)
	port.write(fullTemp)
	port.write(fullCond)
	port.write(fullTimeP1)
    port.write(fullDust)
	port.write(fullmDust)

