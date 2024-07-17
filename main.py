import streamlit as st
import mysql.connector as mysql
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

    

def insert_data(x1,x2,x3,x4,x5,x6,x7):
    
    #Establishing connection to mysql
    cnx = mysql.connect(user='root', password='AccountsandRoles@78',
                        host='127.0.0.1',
                        database='zoho_pretest',
                        use_pure=False)
    cursor=cnx.cursor()
    
    add_user = ("INSERT INTO user_details "
                "(first_name, last_name, gender, birth_date, age, email_id, password) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    #initialize the arguments before executing
    #data_user = ('Geert', 'Vanderkelen', 'M', date(1977, 6, 14),35,'asde@gmail.com','12345')
    data_user = (x1,x2,x3,x4,x5,x6,x7)
    
    # Insert new user
    cursor.execute(add_user, data_user)
    cnx.commit()
    cursor.close()
    cnx.close()

with st.form("my_form"):
    st.write("Register")
    mail=st.text_input('Enter mail id: ')
    password=st.text_input('Enter password: ',type='password')
    re_password=st.text_input('Renter password: ',type='password')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
       #st.write("slider", slider_val, "checkbox", checkbox_val)
        if password==re_password:
            st.success('Your account has been created!!!')
            st.subheader('Add more details')
            f_name=st.text_input('Enter your first name: ')
            l_name=st.text_input('Enter your last name: ')
            gender=st.selectbox('Gender',['M','F'])   
            dob=st.date_input('Enter your date of birth: ')
            
            by=int(str(dob).split('-')[0])
            bm=int(str(dob).split('-')[1])
            bd=int(str(dob).split('-')[2])
            dob_m=date(by,bm,bd)
            age=st.number_input('Enter your age: ',min_value=1,max_value=100,value=None,placeholder="Type a number...")
            if age:
                st.write(dob_m)
                insert_data(f_name,l_name,gender,dob_m,age,mail,password)
                st.success('Data Inserted')
            
            
            
        
        