import pandas as pd

path = '../attendence_excel.xls'

file = pd.ExcelFile(path)
data = pd.read_excel(file, '23-12-2023')
print(data)

emails = []
count = data.shape
rows = count[0]
print(rows)

print(data['Email'].loc[data.index[0]])

for i in range(rows):
   emails.append(data['Email'].loc[data.index[i]])

print(emails)
