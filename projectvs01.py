import streamlit as st
import pandas as pd

st.image('./img/1.jpeg')
st.header("การนำเสนอสถิติการเกิดอุบัติเหตุของประเทศไทย")

col1,col2=st.columns(2)

with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("2,5600")
with col2:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("2,5600")        