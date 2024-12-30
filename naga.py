import streamlit as st
import os
from streamlit_option_menu import option_menu
import mysql.connector
con=mysql.connector.connect(user="root",host="localhost",port=3306,database="sigma")
from tabulate import tabulate
import pandas as pd

st.title("BETA hospital")
st.text("12/a ayaanar lovil main road madurai-2")
st.divider()


st.image(os.path.join(os.getcwd(),"image","hospital.webp"),width=500)


st.write("""
**Healthcare Services**: Hospitals provide a wide range of medical services, including emergency care, surgery, diagnostics, and specialized treatments. They are equipped with medical professionals such as doctors, nurses, and specialists to handle various health conditions.
""")




st.write("""
**Medical Equipment and Facilities**: Hospitals are equipped with advanced medical technologies and facilities, such as operating rooms, intensive care units (ICU), imaging devices (X-ray, MRI), and laboratories to support diagnosis and treatment.
""")




st.write("""
**Inpatient and Outpatient Care**: Hospitals offer both inpatient care (where patients stay overnight or longer for treatment) and outpatient care (where patients visit for consultations or procedures but return home the same day).
""")
st.divider()

st.subheader("reception")
st.image(os.path.join(os.getcwd(),"image","reception.jpg"),width=600)
st.divider()

st.write("""
**Reception in Hospitals**: The reception area is the first point of contact for patients and visitors entering a hospital. It is typically staffed by receptionists who assist with patient registration, appointment scheduling, and providing information about hospital services. The reception area plays a key role in ensuring smooth patient flow, answering inquiries, directing patients to the appropriate departments, and offering support during hospital visits.
""")
st.divider()



st.subheader("parking facility")
st.image(os.path.join (os.getcwd(),"image","parking.jpeg"),width=600)


st.write("""
**Parking Facility**: Many hospitals provide dedicated parking areas for patients and visitors, ensuring convenience and accessibility. These parking facilities often include both outdoor and indoor parking spaces, with designated areas for emergency vehicles. Some hospitals also offer valet parking services and parking structures to accommodate a large number of vehicles, ensuring smooth access to the hospital.
""")
st.divider()

st.subheader("nursing")
st.image(os.path.join(os.getcwd(),"image","post-nursing.jpg"),width=600)


st.write("""
**Nursing in Hospitals**: Nurses play a crucial role in patient care, providing essential services such as administering medications, monitoring vital signs, assisting with medical procedures, and offering emotional support. Hospital nurses work closely with doctors and other healthcare professionals to ensure comprehensive care for patients. They are available around the clock, often specializing in different areas like critical care, pediatrics, or surgical nursing.
""")
st.divider()

st.subheader("operation theatre")
st.image(os.path.join(os.getcwd(),"image","operation theatr.jpg"),width=600)


st.write("""
**Operation Theater in Hospitals**: The operation theater (OT) is a specially designed and sterile environment within a hospital where surgical procedures are performed. It is equipped with advanced medical equipment, surgical instruments, and proper lighting to ensure the safety and success of surgeries. Skilled surgeons, anesthesiologists, and nursing staff work in the OT to carry out both routine and complex surgeries while maintaining strict hygiene and infection control practices.
""")
st.divider()





with st.sidebar:
    selected=option_menu(
        menu_title="admin panel",
        options=["patient information"," patient detail update", "doctor specialist"],
        icons=["list-check","house-up","suit-heart"],
        menu_icon=["bricks"]
        
    )
if selected=="patient information":
    st.title(f"patient detalis ")
    #name=st.text_input("enter name:")
    #age=st.number_input("enter age",min_value=0)
    #if st.button("summit"):
       #st.success("succesfull")
    res=con.cursor()
    Sql="select * from hospital"
    res.execute(Sql)
    result=res.fetchall()
    
    #print(tabulate(result,headers=["ia","name","dob","address","phone","guardian","problem","doctor","expense"]))
    df=pd.DataFrame(result)
    st.write(df)
    
    
elif selected==" patient detail update":
    st.title(f"details updtate")
    col1,col2,=st.columns(2)
    with col1:
     name=st.text_input("enter a name:")
    with col2: 
     dob=st.date_input("enter date:")
    col1,col2,=st.columns(2)
    with col1:
     address=st.text_input("enter address:")
    with col2:
     phone=st.text_input("enter number:")
    col1,col2,=st.columns(2)
    with col1: 
     guardian=st.text_input("guardian name:")
    with col2: 
     problem=st.text_input("what symptoms:")
    col1,col2,=st.columns(2)
    with col1:

     doctor=st.text_input("doctor name:")
    with col2: 
     expense=st.text_input("amount:")

    if st.button("summit"):
        st.success("updated successfully")
        res=con.cursor()
        sql="insert into hospital(name,dob,address,phone,guardian,problem,doctor,expense)values(%s,%s,%s,%s,%s,%s,%s,%s)"
        res.execute(sql,((name,dob,address,phone,guardian,problem,doctor,expense)))
        con.commit()
        st.write(res)


elif selected=="doctor specialist":
    st.title(f"doctors")
    st.subheader("alagappan")
    st.text("age:46")
    st.text("specialist:ear and nuerology")
    st.text("1 pm to 6 pm")

    st.subheader("geetha")
    st.text("age:56")
    st.text("specialist:leg")
    st.text("8 pm to 11pm")
    
    st.subheader("murugan")
    st.text("age:67")
    st.text("specialist:brain")
    st.text("1 am to 6 pm")
        
    st.subheader("priya")
    st.text("age:35")
    st.text("specialist:gynocologist")
    st.text("5 pm to 10pm")
    
   
