import pandas as pd 

file_path = "/content/Test - input-applicant.xlsx"
excel = pd.ExcelFile(file_path)

ex1 = pd.read_excel(excel,sheet_name='transactions')
ex2 =  pd.read_excel(excel,sheet_name='UserName')
ex3 =  pd.read_excel(excel,sheet_name='Name')
ex4 =  pd.read_excel(excel,sheet_name='Output ')

transactions = pd.DataFrame(ex1)
username = pd.DataFrame(ex2)
name = pd.DataFrame(ex3)
output = pd.DataFrame(ex4)

user_usecount = transactions.groupby('userId')['date'].count()
count = user_usecount.reset_index().rename(columns={'date':'using_times'})
count.head(10)