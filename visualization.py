import json
import pandas as pd
import matplotlib.pyplot as plt

# Load JSON data from files
with open('query_result/top_demanded_skills.json', 'r') as file:
    top_demanded_skills = json.load(file)

with open('query_result/top_skills_based_on_salary.json', 'r') as file:
    top_skills_based_on_salary = json.load(file)

with open('query_result/top_paying_job_skills.json', 'r') as file:
    top_paying_job_skills = json.load(file)

# Convert JSON data to DataFrames
df_demanded_skills = pd.DataFrame(top_demanded_skills)
df_skills_salary = pd.DataFrame(top_skills_based_on_salary)
df_paying_jobs = pd.DataFrame(top_paying_job_skills)

# Convert 'counts' and 'avg_salary' columns to numeric types
df_demanded_skills['counts'] = pd.to_numeric(df_demanded_skills['counts'])
df_skills_salary['avg_salary'] = pd.to_numeric(df_skills_salary['avg_salary'])

# Visualization 1: Top Demanded Skills for Data Analysts
plt.figure(figsize=(10, 6))
plt.bar(df_demanded_skills['skills'], df_demanded_skills['counts'], color='skyblue')
plt.title('Top Demanded Skills for Data Analysts')
plt.xlabel('Skills')
plt.ylabel('Demand Count')
plt.xticks(rotation=45)

plt.savefig('./assets/top_demanded_skills.png', bbox_inches='tight', dpi=300)  # dpi=300 for high resolution
plt.show()
plt.close()

# Visualization 2: Top Skills Based on Average Salary
plt.figure(figsize=(10, 6))
plt.barh(df_skills_salary['skills'], df_skills_salary['avg_salary'], color='lightgreen')
plt.title('Top Skills Based on Average Salary for Data Analysts')
plt.xlabel('Average Salary ($)')
plt.ylabel('Skills')
plt.gca().invert_yaxis()
plt.savefig('./assets/top_skills_based_on_salary.png', bbox_inches='tight', dpi=300)  # dpi=300 for high resolution
plt.show()
plt.close()

