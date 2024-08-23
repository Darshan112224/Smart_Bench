import getpass
import smtplib



import pandas as pd
file_name = input("Enter date: ")
path = './data/attendence_excel.xls'

file = pd.ExcelFile(path)
data = pd.read_excel(file, file_name)

data = data.drop_duplicates()
emails = []
count = data.shape
rows = count[0]


for i in range(rows):
   emails.append(data['Email'].loc[data.index[i]])







HOST = "smtp.gmail.com"
PORT ="587"

F_EMAIL = "thedarshan1611@gmail.com"


PASSW = 'bknb pjkv hqko eicy'

msg = "Your child is present today"
smtp = smtplib.SMTP(HOST, PORT)

status_code, res = smtp.ehlo()
print(f"{status_code} {res}")

status_code, res = smtp.starttls()
print(f"{status_code} {res}")

status_code, res = smtp.login(F_EMAIL,PASSW)
print(f"{status_code} {res}")




for i in emails:
    T_EMAIL = i
    smtp.sendmail(F_EMAIL,T_EMAIL,msg)

smtp.quit()
