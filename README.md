# garbageCalendar
Little python script to create an ics-import for google calendar with the dates of the garbage disposal.

Usage: 
1) Enter the dates from your garbage-disposal company in input/dates.json. 
2) Run 'python garbageCalendar.py'
3) Import 'output/calendarImport.ics' in your google-calendar

Hints: the best is to create an own calendar for your garbage-disposal. If you want you can activate notifications there for all dates in the calendar. It is not possible
to create notification-events on generated calendar-items cause of a topic with the UID in the ICS-File.

And yes ... i know sometimes you can find ics-imports on the company websites ... but this year the download failed there and i wanted to learn something in python ;)

