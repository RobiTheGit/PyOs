from datetime import date
import calendar
import subprocess
subprocess.run('clear')
todays_date = date.today()
year = todays_date.year
calendar = calendar.calendar(year, w=2, l=1, c=6, m=3)

print(calendar)
input('press enter to exit.')
