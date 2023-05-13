import streamlit as st
import pandas as pd


st.title('IOE Aggregate Percentage Calculator for BCT')



x1 = st.number_input('Enter your 1st sem total marks', value= 0)
x2 = st.number_input('Enter your 2nd sem total marks', value= 0)
x3 = st.number_input('Enter your 3rd sem total marks', value= 0)
x4 = st.number_input('Enter your 4th sem total marks', value= 0)
x5 = st.number_input('Enter your 5th sem total marks', value= 0)
x6 = st.number_input('Enter your 6th sem total marks', value= 0)
x7 = st.number_input('Enter your 7th sem total marks', value= 0)
x8 = st.number_input('Enter your 8th sem total marks', value= 0)


operation = st.button('Calculate Aggregate Percentage')
if operation:
    result = ((x1*10)/725)+((x2*10)/650)+((x3*10)/875)+((x4*10)/900)+((x5*15)/875)+((x6*15)/825)+((x7*15)/825)+((x8*15)/750)
    result1 = round(result, 3)
    st.write(f'Your Aggregate Percentage = {result1}%')



