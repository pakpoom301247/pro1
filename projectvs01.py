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

dt=pd.read_excel('data/opendata-rtddi-54-66-9month.xlsx')    

st.write(dt.head(1))

#st.write()
NumM=dt[dt['Sex']=='ชาย'].count()
NumF=dt[dt['Sex']=='หญิง'].count()

st.subheader('ชาย')
st.subheader(NumM[1])
st.subheader('หญิง')
st.subheader(NumF[1])
dtSex=[NumM[1],NumF[1]]
dtSexd=pd.DataFrame(dtSex,index=["ชาย","หญิง"])
st.bar_chart(dtSexd)

import matplotlib.pyplot as plt
labels = 'man', 'woman'
sizes = [NumM[1],NumF[1]]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)