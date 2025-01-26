import pandas as pd

csvData = pd.read_csv("RollNo_Name_Assignment.txt",sep="\t") 

csvData.sort_values(["rollScoreQuiz1.txt"], axis=0, ascending=[True], inplace=True) 
print(csvData)