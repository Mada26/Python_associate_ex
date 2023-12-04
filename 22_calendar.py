from calendar import Calendar
import calendar

class MyCalendar(Calendar):
    def __init__(self):
        super().__init__(self)  

    def count_weekday_in_year(self,year,weekday):
        cnt=0
        d=[]
        for wd in self.monthdays2calendar(year,weekday):
            d.append(wd)
        for i in len(d):
            for j in len(d[i]):
                for x in len(d[i[j]]):
                    if d[i[j[x]]]==0:
                        cnt+=1
        print(cnt)

ob=calendar.MyCalendar()
ob.count_weekday_in_year(2019,0)