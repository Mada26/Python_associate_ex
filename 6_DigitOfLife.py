
date=""



def inputDate():
    global date
    date=input("input your  birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY:  ")

inputDate()

def Digit():
    global date
    counter=0
    if date.isdigit():
        date=list(date)
        for i in date:
            counter+=int(i)
        

    else:
        print("its not the right format")
        inputDate()
        Digit()
        
    print(counter)

Digit()
    
            