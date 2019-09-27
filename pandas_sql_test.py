from env import host, user, password
import pandas as pd

def get_db_url(username, hostname, password, database):
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return url

#Don't forget to change your db. I might just hard code it up there.

df = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)
print(df)







# Getting data from SQL databases

# Use your function to obtain a connection to the employees database.
# Once you have successfully run a query:
# Intentionally make a typo in the database url. What kind of error message do you see?
# Intentionally make an error in your SQL query. What does the error message look like?
# Read the employees and titles tables into two separate dataframes
# Visualize the number of employees with each title.
# Join the employees and titles dataframes together.
# Visualize how frequently employees change titles.
# For each title, find the hire date of the employee that was hired most recently with that title.
# Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL and python/pandas code)