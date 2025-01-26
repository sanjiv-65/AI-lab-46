l=[]
f=open("test.txt","r")
for i in f.readlines():
    l.append(i.split("\t")[0].rstrip("\n"))
print(l)