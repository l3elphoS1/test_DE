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

#แปลง พศ เป็น คศ 
def be_to_ad(be_date_str):
    # Parse the date in Buddhist Era format
    date_buddhist = datetime.strptime(be_date_str, '%m/%d/%Y %H:%M:%S')
    
    # Convert the Buddhist year to Gregorian year
    ad_year = date_buddhist.year - 543
    
    # Return the converted date in Gregorian format
    return date_buddhist.replace(year=ad_year).strftime('%d/%m/%Y')

# สร้าง column ใหม่ ที่เป็นคศ
transactions['gregorian_date'] = transactions['date'].apply(be_to_ad)

# หา latest date เพื่อนำมาลบกับ date หา diff 
transactions['max_dates'] = transactions.groupby('userId')['date'].max()

transactions['diff_date'] = (transactions['max_dates'] - transactions['gregorian_date']).dt.days

transactions.head()