result={}

try:
    user=input(" introdu numele fisierului, cu extensie ")
    s=open(user,"w+t")
    s.write("aBc")
    s.close()
    c=open(user,"rt")
    for l in c:
            for ch in l:
                ch.lower()
                result.update({ch:0})
                for k in result.keys():
                     if ch==k:
                          result[k]+=1
    sortednames=sorted(result.keys(), key=lambda x:x.lower())
    print(sortednames)
except:
    print("there is no file")
            