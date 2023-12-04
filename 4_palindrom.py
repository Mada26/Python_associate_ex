print("input your text here")
text=input()
text=text.lower().strip()
text=list(text)
counter =0

for i in range(0,(int(len(text)/2))):
    if text[i]==text[len(text)-1-i]:
        counter+=1
    
if counter==int((len(text)/2)):
    print("e palindrom")
else:
    print("nu e palindrom")