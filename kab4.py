import pandas as pd

main_df = pd.read_csv('RollNo_Name_Assignment.txt', delimiter='\t')
quiz1_df = pd.read_csv('RollNo_Score_Quiz_1.txt', delimiter='\t')
quiz2_df = pd.read_csv('RollNo_Score_Quiz_2.txt', delimiter='\t')
viva_df = pd.read_csv('Name_Viva.txt', delimiter='\t')

main_df = pd.merge(main_df, quiz1_df, on='Roll No', how='left')
main_df = pd.merge(main_df, quiz2_df, on='Roll No', how='left')
main_df = pd.merge(main_df, viva_df, left_on='Name', right_on='Name', how='left')

main_df.rename(columns={
    'Score_x': 'Assignment Score',
    'Number Obtained_x': 'Quiz 1 Score',
    'Number Obtained_y': 'Quiz 2 Score',
    'Score_y': 'Viva Score'
}, inplace=True)

main_df.fillna({'Quiz 1 Score': 0, 'Quiz 2 Score': 0, 'Viva Score': 0}, inplace=True)

main_df['Total Score'] = (
    main_df['Assignment Score'] +  
    main_df['Quiz 1 Score'] +
    main_df['Quiz 2 Score'] +
    main_df['Viva Score']
)

total_full_marks = 5 + 15 + 15 + 15  # Full marks for all components
# Function to calculate grade
def calculate_grade(score, full_mark):
    percentage = (score / full_mark) * 100
    if percentage >= 90:
        return 'O'
    elif percentage >= 80:
        return 'E'
    elif percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

# Apply grade calculation
main_df['Grade'] = main_df['Total Score'].apply(lambda x: calculate_grade(x, total_full_marks))

# Create email column
main_df['Email'] = main_df['Roll No'].astype(str) + '@gmail.com'

# Select required columns
final_df = main_df[['Name', 'Roll No', 'Total Score', 'Grade', 'Email']]

# Save the final dataframe to CSV
final_df.to_csv('Final_Score_Sheet.csv', index=False)
print("Final score sheet saved as 'Final_Score_Sheet.csv'.")
