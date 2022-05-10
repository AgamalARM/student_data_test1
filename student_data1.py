# -*- coding: utf-8 -*-
"""
Created on Tue May 10 09:23:00 2022

@author: Gamal
"""

####  import Lib ######

import streamlit as st
import pandas as pd
import numpy as np
import csv

# ###############   Banner ################
# st.title("Dexcom Students Data Entry System")
# ########   Login ##################


# file = open("student_data.csv")
# csvreader = csv.reader(file)
# header = next(csvreader)
# print(header)
# rows = []
# for row in csvreader:
#     rows.append(row)
# print(rows)
# file.close()
#######   reading pervious data  #######
st.write("## Show Pervious Data")
file1 = open("student_data.csv")
df_students = pd.DataFrame(file1)   
#df_students = pd.read_csv("student_data.csv")
st.write(df_students)
st.write(df_students.shape)
file1.close()

student_id = st.sidebar.text_input("Student ID")
student_name = st.sidebar.text_input("Student Name")
student_phone = st.sidebar.text_input("Student Phone Number")
student_email = st.sidebar.text_input("Student Email")
student_class_name = st.sidebar.text_input("Student Class Name")
student_subject = st.sidebar.text_input("Student Subject")

@st.cache(allow_output_mutation=True)
def get_data():
    return []


##reading_value = st.sidebar.number_input('The reading from Dexcom sensor')


if st.button("Add Student"):
    get_data().append({"Student_ID": student_id, 
                       "Student_Name": student_name, 
                       "Student_Phone": student_phone,
                       "Student_Email": student_email,
                       "Student_Class_Name": student_class_name,
                       "Student_Subject": student_subject})

df_students = pd.DataFrame(get_data())
st.write("## Show New Data")
st.write(df_students)
st.write(df_students.shape)

### convert df to csv and save it    ###
def convert_df(df_students):
   return df_students.to_csv().encode('utf-8')


csv1 = convert_df(df_students)
st.write(csv1)

file2 = open('student_data.csv')
df_students.to_csv (r'student_data.csv', index = False, header=True)
file2.close()

# import csv

# # open the file in the write mode
# f = open('student_data.csv', 'w')

# # create the csv writer
# writer = csv.writer(f)

# # write a row to the csv file
# #writer.writerow(row)

# # close the file
# f.close()
