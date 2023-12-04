print("input your Sudoku ")

lista=[]
seDubleaza=0
for i in range(0,9):
    numar=list(input())

#Checks on LINE

    #check the length of the line input, must be 9
    if len(numar)!=9:
        print("format incorect")
        break
        
    else:
        #check line for dubplicats
        for j in range(0,len(numar)-1):
            for x in range(j+1,len(numar)):
            
                if numar[j]==numar[x]:
                    seDubleaza+=1
        if seDubleaza!=0:
            print("format incorect")
            break
        lista.append(numar)

seDubleaza=0
#Checks on COLLUMN
for i in range (0,9):
    for j in range (i+1,9):
        if lista[i][i]==lista[j][i]:
            seDubleaza+=1
if seDubleaza!=0:
    print("format incorect")
    exit()

#schec 3x3 square
seDubleaza=0
toDelete=[]

def sq():
    global seDubleaza
    for i in range (0,3):
        for j in range(0,3):
            if lista[0][i]==lista[1][j] or  lista[0][i]==lista[2][j] or lista[1][i]==lista[2][j]:
                seDubleaza+=1
    
            
    if seDubleaza!=0:
        print("format incorect")
        print(seDubleaza)
    elif seDubleaza==0:
        for i in range(0,3):
            for j in range(0,3):
                a=lista[i][j]
                lista[i].remove(a)
        print(lista)

for i in range(0,9):
    sq()



