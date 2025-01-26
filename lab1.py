#Read the files using 'readlide_returnList' function given in 'read_file.py' code.
#Print the name of the student one by one.
#Sort all the name of the student in two student list.
#Count how many times 'PRIYANSHU' and 'HIMANSHU' present in the first student list.
#Merge the two student list.
#Remove the duplicate valuse present in student list.
# Import the readlide_returnList function from read_file.py
with open ("student1.csv") as f:
     for i in f:
         print(f.readline(), end="")

import pandas as pd
df = pd.read_csv("student1.csv", names=["Name"]) 
df = df.sort_values(by="Name", ascending=True, kind="quicksort", na_position="last")
print(df.head(46))