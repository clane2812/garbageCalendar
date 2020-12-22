import json

monthOfYear = ["januar","februar","march","april","may","june","july","august","september","october","november","december"]
icsheader = """BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Müll
X-WR-TIMEZONE:Europe/Berlin
"""
icstemplate = """
BEGIN:VEVENT
DTSTART;VALUE=DATE:#DATEPATTERN
DTEND;VALUE=DATE:#DATEPATTERN
DTSTAMP:20201220T112509Z
UID:garbageCalendar_#UIDPATTERN 
CLASS:PUBLIC
CREATED:20201221T010542Z
DESCRIPTION:created by garbage calendar
LAST-MODIFIED:20201221T122537Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:#LABELPATTERN 
TRANSP:TRANSPARENT
END:VEVENT
"""

def createDate(datelabel,label):
    global uidCounter
    date = icstemplate
    date = date.replace("#DATEPATTERN",datelabel)
    date = date.replace("#LABELPATTERN",label)
    date = date.replace("#UIDPATTERN",str(uidCounter))
    uidCounter+=1
    outfile.write(date)

file = open(".\\input\\dates.json",mode='r',encoding='UTF-8')  
data = json.load(file)
file.close()
outfile = open(".\\output\\calendarImport.ics",'w')
outfile.write(icsheader)
uidCounter=1

for trashbin in data:
    print("creating calender dates for {}".format(trashbin))
    for month in data[trashbin]:
        if month in monthOfYear:
            print(month + ":")
            for day in data[trashbin][month]:
                datelabel = "2021{:02d}{:02d}".format(monthOfYear.index(month)+1,day)
                print(datelabel);
                createDate(datelabel,trashbin)
        else:
            print("found unknown month {} in input file".format(month))

outfile.write("END:VCALENDAR")
outfile.close()
        


