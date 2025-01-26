with open ("student1.csv") as f:
     for i in f:
         print(f.readline(), end="")

    
import pandas as pd
df = pd.read_csv("student1.csv", names=["Name"])
df = df.sort_values(by="Name", ascending=True, kind="quicksort", na_position="last")
print(df.head(46))

