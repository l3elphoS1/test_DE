import pandas as pd 
from datetime import datetime

file_path = "./Test - input-applicant.xlsx"
excel = pd.ExcelFile(file_path)

ex1 = pd.read_excel(excel,sheet_name='transactions')
ex2 =  pd.read_excel(excel,sheet_name='UserName')
ex3 =  pd.read_excel(excel,sheet_name='Name')
ex4 =  pd.read_excel(excel,sheet_name='Output ')

transactions = pd.DataFrame(ex1)
username = pd.DataFrame(ex2)
name = pd.DataFrame(ex3)
output = pd.DataFrame(ex4)



# Convert Buddhist Era (BE) to Gregorian (AD)
def be_to_ad(be_date_str):
    # Parse the date in Buddhist Era format
    date_buddhist = datetime.strptime(be_date_str, '%m/%d/%Y %H:%M:%S')
    
    # Convert the Buddhist year to Gregorian year
    ad_year = date_buddhist.year - 543
    
    # Return the converted date in Gregorian format
    return date_buddhist.replace(year=ad_year)

# Create a new column with Gregorian date
transactions['gregorian_date'] = transactions['date'].apply(be_to_ad)

# Ensure the 'gregorian_date' is in datetime format before calculating the date difference
transactions['gregorian_date'] = pd.to_datetime(transactions['gregorian_date'], format='%m/%d/%Y')

# Calculate the latest date for each user and find the difference with the 'gregorian_date'
transactions['max_dates'] = transactions.groupby('userId')['gregorian_date'].transform('max')

transactions['diff_date'] = (transactions['max_dates'] - transactions['gregorian_date']).dt.days

# Show the first few rows
transactions.head()
