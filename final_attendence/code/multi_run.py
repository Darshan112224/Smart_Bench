import face_recognition
import cv2
import numpy as np
import os
import xlwt
from xlwt import Workbook
from datetime import date
import xlrd, xlwt
from xlutils.copy import copy as xl_copy








"""CurrentFolder = os.getcwd() #Read current folder path
image = CurrentFolder+'\\images\\darshan.jpeg'
image2 = CurrentFolder+'\\images\\jay.jpeg'
image3 = CurrentFolder+'\\images\\aamir.jpeg'"""

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is not required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
video_capture_1 = cv2.VideoCapture(1,cv2.CAP_DSHOW)


# Load a sample picture and learn how to recognize it.
import json

with open('./data/student_data.json', mode='r') as f:

    json_data = json.load(f)

known_face_names = []
known_face_email =[]
known_face_enrollments = []
known_face_department = []
known_face_semester = []
image_addresses = []
# We start to iterate over each dictionary in our list
for json_dict in json_data:
    # We append each name value to our result list
    known_face_names.append(json_dict['Name'])
    known_face_email.append(json_dict['Email'])
    known_face_enrollments.append(json_dict['Enroll'])
    known_face_department.append(json_dict['Department'])
    known_face_semester.append(json_dict['Semester'])
    image_addresses.append(json_dict['img_path'])


print(known_face_names)
print(known_face_email)
print(image_addresses) 




known_face_encodings = []

for i in image_addresses:
    print(i)
    person_image = face_recognition.load_image_file(i)
    known_face_encoding = face_recognition.face_encodings(person_image)[0]
    known_face_encodings.append(known_face_encoding)
print(known_face_encodings)


"""person1_name = "Darshan"
person1_image = face_recognition.load_image_file(image)
person1_face_encoding = face_recognition.face_encodings(person1_image)[0]
person1_email = "201240116018.it@gmail.com"

# Load a second sample picture and learn how to recognize it.
person2_name = "Jay"
person2_image = face_recognition.load_image_file(image2)
person2_face_encoding = face_recognition.face_encodings(person2_image)[0]
e2 = "201240116017.it@gmail.com"

# Load a third sample picture and learn how to recognize it.
person3_name = "amir"
person3_image = face_recognition.load_image_file(image3)
person3_face_encoding = face_recognition.face_encodings(person3_image)[0]
e3 = "201240116013.it@gmail.com"
"""
# Create arrays of known face encodings and their names
"""person1_face_encoding,
    person2_face_encoding,
    person3_face_encoding"""












"""known_face_names = [
    person1_name,
    person2_name,
    person3_name
] 
known_face_email = [
    person1_email,
    e2,
    e3
]"""

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []

face_locations1 = []
face_encodings1 = []
face_names1 = []
process_this_frame = True

rb = xlrd.open_workbook('./data/attendence_excel.xls', formatting_info=True) 
wb = xl_copy(rb)
inp = input('Please give Date')
sheet1 = wb.add_sheet(inp)
sheet1.write(0, 0, 'Name')
#sheet1.write(0, 1, str(date.today()))
sheet1.write(0, 1, 'Enrollment')
sheet1.write(0,2, 'Email')
sheet1.write(0,3, 'Department')
sheet1.write(0,4, 'Semester')
row=0
col=0
already_attendence_taken = []
while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()
            ret_1, frame_1 = video_capture_1.read()


            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            small_frame_1 = cv2.resize(frame_1, (0, 0), fx=0.25, fy=0.25)


            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            rgb_small_frame_1 = small_frame_1[:, :, ::-1]


            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                face_locations1 = face_recognition.face_locations(rgb_small_frame_1)
                face_encodings1 = face_recognition.face_encodings(rgb_small_frame_1, face_locations1)

                face_names = []
                face_names1 = []
                if ret :
                    for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                            email = known_face_email[best_match_index]
                            enroll = known_face_enrollments[best_match_index]
                            dept = known_face_department[best_match_index]
                            sem = known_face_semester[best_match_index]

                        face_names.append(name)
                        if((enroll not in already_attendence_taken) and (name != "Unknown")):
                            row = row+1
                            sheet1.write(row, col, name )
                            col =col+1
                            sheet1.write(row, col, enroll )
                            col = col+1
                            sheet1.write(row,col,email)
                            col =col+1
                            sheet1.write(row, col, dept )
                            col =col+1
                            sheet1.write(row, col, sem )

                            col = 0
                            print("attendence taken for " + name)
                            wb.save('./data/attendence_excel.xls')
                            already_attendence_taken.append(enroll)
                            print(already_attendence_taken)
                        else :
                            print("")
           
                if ret_1:
                    for face_encoding in face_encodings1:
                    # See if the face is a match for the known face(s)
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                            email = known_face_email[best_match_index]
                            enroll = known_face_enrollments[best_match_index]
                            dept = known_face_department[best_match_index]
                            sem = known_face_semester[best_match_index]
                        face_names1.append(name)
                        if((enroll not in already_attendence_taken) and (name != "Unknown")):
                            row = row+1
                            sheet1.write(row, col, name )
                            col =col+1
                            sheet1.write(row, col, enroll )
                            col = col+1
                            sheet1.write(row,col,email)
                            col =col+1
                            sheet1.write(row, col, dept )
                            col =col+1
                            sheet1.write(row, col, sem )
                     
                            col = 0
                            print("attendence taken for " + name)
                            wb.save('./data/attendence_excel.xls')
                            already_attendence_taken.append(enroll)

                        else :
                            print("")
                
            process_this_frame = not process_this_frame


            # Display the results
            if ret:
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                # Draw a box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        


                # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

              
            if ret_1:
                for (top, right, bottom, left), name in zip(face_locations1, face_names1):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                # Draw a box around the face
                    cv2.rectangle(frame_1, (left, top), (right, bottom), (0, 0, 255), 2)


                # Draw a label with a name below the face
                    cv2.rectangle(frame_1, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame_1, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)



            # Display the resulting image
            if ret:
                cv2.imshow('Video', frame)
            if ret_1:
                cv2.imshow('Video1', frame_1)


            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xff==ord('q'):   
                print("data save")
                break

# Release handle to the webcam
video_capture.release()
video_capture_1.release()

cv2.destroyAllWindows()
