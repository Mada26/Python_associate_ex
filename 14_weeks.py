class WeekDayError(Exception):
    pass
	

class Weeker:
    #
    # Write code here.
    #
    days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    present=False

    def __init__(self, day):
        #
        # Write code here.
        #
        self.day=day
        for d in self.days:
            if d==self.day:
                self.present=True
        if self.present==False:
            raise WeekDayError 
        

    def __str__(self):
        #
        # Write code here.
        #
        return self.day
        
    def add_days(self, n):
        #
        # Write code here.
        #
        self.n=n
        next=int(self.n)
        index=next%7
        self.day=self.days[index]
        return self.day
    
    def subtract_days(self, n):
        #
        # Write code here.
        #
        self.n=n
        next=int(self.n)
        index=next%7
        self.day=self.days[8-index]
        return self.day

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
