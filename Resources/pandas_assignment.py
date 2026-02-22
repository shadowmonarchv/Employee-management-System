import pandas as pd

# 1. Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}
df = pd.DataFrame(data)

# a. First 5 rows
print(df.head())

# b. Summary statistics
print("\nSummary Statistics:\n", df[['Age', 'Salary']].describe())

# c. Average salary in HR
avg_hr_salary = df[df['Department'] == 'HR']['Salary'].mean()
print(f"\nAverage HR Salary: {avg_hr_salary}")

# 2. Add 'Bonus' column (10%)
df['Bonus'] = df['Salary'] * 0.10

# 3. Filter Age 25-30
filtered_df = df[(df['Age'] >= 25) & (df['Age'] <= 30)]
print("\nEmployees aged 25-30:\n", filtered_df)

# 4. Group by Department
dept_avg = df.groupby('Department')['Salary'].mean()
print("\nAvg Salary by Dept:\n", dept_avg)

# 5. Sort and Save
sorted_df = df.sort_values(by='Salary', ascending=True)
sorted_df.to_csv(, index=False)