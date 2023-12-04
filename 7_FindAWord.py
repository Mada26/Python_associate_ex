text1=input("input your word  ")
text2=input("input big text  ")

counter=0

for i in text1:
    for j in text2:
        if i==j:
            counter+=1
if counter==len(text1):
    print("yes")

else:
    print("no")