print("input 2 words")
text1=input()
text2=input()

#remove white spaces
text1=list(text1.lower().strip())
text2=list(text2.lower().strip())

counter=0

#chech if it's the same lenght

if len(text2)!=len(text1):
    print("are not anagrams1")

else:
    for i in range(0,len(text1)):
        for j in range(0,len(text2)):
            if text1[i]==text2[j]:
                counter+=1
        
if counter== int(len(text1)):
    print("anagrama")

else:
    print("are not anagrams2")