import json
import subprocess
from os import path
 
filename = './data/student_data.json'
listObj = []

#take input
name = input('Enter name: ')
enroll_s = input('Enter Enrollment no.: ')
email = input('Enter email: ')
sem = input('Enter Semeester in digit(ex: 7 ): ')
dept_r = input('Enter Department (in short form): ')
enroll = int(enroll_s)
dept = dept_r.upper()




# Check if file exists
if path.isfile(filename) is False:
  raise Exception("File not found")
 
# Read JSON file
with open(filename) as fp:
  listObj = json.load(fp)
 
# Verify existing list
print(listObj)
print(type(listObj))
 
listObj.append({
  "Name": name,
  "Enroll": enroll,
  "Email": email,
  "img_path":'data\images\i_' + enroll_s +'.png',
  "Department": dept,
  "Semester": sem
})
 
# Verify updated list
print(listObj)
 
with open(filename, 'w') as json_file:
    json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))
 
print('Successfully appended to the JSON file')

subprocess.call("save_image.exe")