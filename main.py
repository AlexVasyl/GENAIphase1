import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

# Question 1

overdue_rows = df[df['OverDue'] == True]
overdue_rowscount = overdue_rows.shape[0]
print("Question 1: The total number of overdue tasks is:", overdue_rowscount)

# Question 2
#contains_open = df['Status'].str.contains('Open', case=False, na=False)
#contains_closed = df['Status'].str.contains('Closed', case=False, na=False)

#combined_mask = contains_open | contains_closed
#filtered_rows = df[combined_mask].copy()

#filtered_rows['SimplifiedStatus'] = filtered_rows['Status'].apply(lambda x: 'Open' if 'Open' in x else 'Closed')
#grouped_counts = filtered_rows.groupby('Task Group')['SimplifiedStatus'].value_counts().unstack().fillna(0)

filtered_rows = df[df['Report Status'].isin(['Open', 'Closed'])]
grouped_counts = filtered_rows.groupby('Task Group')['Report Status'].value_counts().unstack().fillna(0)
print("Question 2: Number of Closed and Open Task based on Task Group:", grouped_counts)

#Question 3

grouped_counts.plot(kind='bar', stacked=False, figsize=(10,6))

plt.title('Number of Open and Closed Tasks by Task Group')
plt.ylabel('Number of Tasks')
plt.xlabel('Task Group')
plt.tight_layout()

# Display the chart
print ("Question 3: Here is the graph!!!!!")
plt.show()
plt.savefig('question3_graph.png')
plt.close()
#Question 4
overdue_by_project = overdue_rows.groupby('project').size().sort_values(ascending=False)
overdue_by_project.plot(kind='bar', figsize=(10,6), color='red', alpha=0.7)

plt.title('Number of Overdue Tasks by Project')
plt.ylabel('Number of Overdue Tasks')
plt.xlabel('Project')
plt.tight_layout()

# Display the chart
print ("Question 4: Here is the graph!!!!!")
plt.show()
plt.savefig('question4_graph.png')
plt.close()
#Question 5

total_tasks_by_project = df.groupby('project').size()
overdue_df = df[df['OverDue'] == True]

overdue_by_project = overdue_df.groupby('project').size()
overdue_percentage_by_project = (overdue_by_project / total_tasks_by_project * 100).fillna(0)

overdue_percentage_by_project.sort_values(ascending=False).plot(kind='bar', figsize=(10,6), color='blue', alpha=0.7)
plt.title('Percentage of Overdue Tasks by Project')
plt.ylabel('Percentage (%)')
plt.xlabel('Project')
plt.tight_layout()

# Display the chart
print ("Question 5: Here is the graph!!!!!")
plt.show()
plt.savefig('question5_graph.png')
plt.close()
#Question 6 Report the mean number of days elapsed since forms were opened by project

df = pd.read_csv('Construction_Data_PM_Forms_All_Projects.csv')
df['Created'] = pd.to_datetime(df['Created'], dayfirst=True)  # Convert the 'created' column to datetime format

# Group by 'project' and find mean of the 'created' column
mean_dates = df.groupby('Project')['Created'].mean()
today = pd.Timestamp.today()
days_elapsed = (today - mean_dates).dt.days

# Plotting using matplotlib
print("Here is table for question 6. Left is Project, right is Days elapsed")
print(days_elapsed)


#Question 7: Create a bar chart of the number of open forms by Type of form
#df = pd.read_csv('Construction_Data_PM_Forms_All_Projects.csv')
open_forms = df[df['Report Forms Status'] == "Open"]
grouped_forms = open_forms.groupby('Type').size().sort_values(ascending=False)

grouped_forms.plot(kind='bar', figsize=(10,6), color='green', alpha=0.7)

plt.title('Number of Overdue Tasks by Type')
plt.ylabel('Number of Overdue Tasks')
plt.xlabel('Type')
plt.tight_layout()
print("Here is Graph for Question 7!!!!!!!!!!!!!!!!!!!!")
plt.show()
plt.savefig('question7_graph.png')
plt.close()
#Questions 8: Create a time series plot of the number of forms
# opened (which are currently open) by Report Form Group. (Optional)


# Assuming df is your DataFrame
# Filter for rows where the form is opened
opened_forms = df[df['Report Forms Status'] == "Open"]

# Group by 'Report Forms Group' and count the number of opened forms
grouped_counts = opened_forms.groupby('Report Forms Group').size()

# Plotting using matplotlib
plt.figure(figsize=(12, 6))
grouped_counts.plot()
plt.title('Number of Opened Forms Over Time Grouped by Report Forms Group')
plt.ylabel('Number of Opened Forms')
plt.xlabel('Report Forms Group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('question8_graph.png')
plt.close()
