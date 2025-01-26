d={1:"A",2:"B",3:"C"}
print(d)
for i in d:
    print(d[i])
d={}
file=open("dictionarrry.txt",'r')
for i in file.readlines():
       d[i.split(" ")[0]]=i.split(" ")[1].rstrip("\n")
print(d)
