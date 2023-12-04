#from calendar import Calendar
import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()  

    def count_weekday_in_year(self,year,weekday):
        cnt=0
        d=[]
        for wd in self.monthdays2calendar(year,weekday):
            d.append(wd)
        for i in range(len(d)):
            for j in range(len(d[i])):
                for x in range(len(d[i][j])):
                    if d[i][j][x]==0:
                        cnt+=1
        return cnt

ob=MyCalendar()
print(ob.count_weekday_in_year(2019,1))