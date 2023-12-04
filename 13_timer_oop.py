class Timer:
    def __init__(self,hours=0,minutes=0,seconds=0):
        #
        # Write code here
        #
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        if self.seconds>=60:
            self.seconds= self.seconds-60
        if self.minutes>=60:
            self.minutes= self.minutes-60
        if self.hours>=24:
            self.hours= self.hours-24

        

    def __str__(self):
        #
        # Write code here
        #
        
        h=str(self.hours)
        m=str(self.minutes)
        s=str(self.seconds)
        if self.seconds<10:
            s="0"+str(self.seconds)
        if self.minutes<10:
            m="0"+str(self.minutes)
        if self.hours<10:
            h="0"+str(self.hours)
        return h+":"+m+":"+s

    def next_second(self):
        #
        # Write code here
        #
        self.seconds+=1

        #when reached 60 increment the rest
        if self.seconds==60:
            self.minutes+=1
        if self.minutes==60:
            self.hours+=1

        #when reached 60 reset to 0    
        if self.seconds>=60:
            self.seconds= self.seconds-60
        if self.minutes>=60:
            self.minutes= self.minutes-60
        if self.hours>=24:
            self.hours= self.hours-24

    def prev_second(self):
        #
        # Write code here
        #
       
        if self.seconds==0:
            self.seconds=60 
        if self.minutes==0:
            self.minutes= 60
        if self.hours==0:
            self.hours= 24
        self.seconds-=1

        if self.seconds==59:
            self.minutes-=1
        if self.minutes==59:
            self.hours-=1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
