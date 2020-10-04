import datetime
import subprocess
import sys
from dateutil.relativedelta import relativedelta
import holidays


# start=(sys.argv[1])
start=str(datetime.date.today())
# end=(sys.argv[2])
end=str(datetime.date.today() + relativedelta(months=6))

start_date = datetime.datetime.strptime(start, '%Y-%m-%d').date()
if start_date.isoweekday() in set((6, 7, 1)):
    start_date += datetime.timedelta(days=12 - start_date.isoweekday())

end_date = datetime.datetime.strptime(end, '%Y-%m-%d').date()
if end_date.isoweekday() in set((6, 7, 1)):
    end_date += datetime.timedelta(days=8 - end_date.isoweekday())
days = end_date - start_date

valid_days = {(start_date + datetime.timedelta(days=x)).isoformat()
    for x in range(days.days+1)
    if ((start_date + datetime.timedelta(days=x)).isoweekday() >= 5 or (start_date + datetime.timedelta(days=x)).isoweekday() == 1)}

v = list(valid_days)
v.sort()
# print(v)
us_holidays = holidays.US()

def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n]
        
def main():
	n = 4
	x = list(divide_chunks(v, n))
	# print(x) 
	for i in range(0,len(x)):
		y = (x[i]) 
		Starting_Date=(y[0])
		Ending_Date=(y[-1])
		print()
		if Starting_Date in us_holidays or Ending_Date in us_holidays:
			nights = 3
		else:
			nights = 2
		hol = us_holidays.get(Starting_Date)
		hol2 = us_holidays.get(Ending_Date)
		print("Starting Date: %s (%s)" % (Starting_Date, hol))
		print("Ending Date: %s (%s)" % (Ending_Date, hol2))
		subprocess.run('python camping.py --start-date %s --end-date %s --nights %d --stdin < parks.txt' % (Starting_Date, Ending_Date, nights), shell=True)
	# print(x)
		
if __name__ == "__main__":
    main()
