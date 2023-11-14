import streamlit as st  
import pandas as pd
import seaborn as sns  
import numpy as np
import matplotlib.pyplot as plt
# a={
#     'name':['abs'],
#     'marks':[25]
#     }

col1,col2,col3=st.columns(3)
col1.metric('Year','$3652','$3201')
col2.metric('India','$4201')


#mining data
df=pd.read_csv('data.csv')
st.title("Data analysis")

#df1=df.drop(['ID','Year','Category','Product','UnitPrice','TotalPrice'],axis='columns')
#st.write(df1)
#st.map(df1)


if st.sidebar.button("load dataset"):  
 st.write(df)

if st.sidebar.button("load description"):  
 st.write(df.describe())

if st.sidebar.button("load description"):  
 st.write(df.describe())

#plot
#a1=pd.DataFrame(df['Year'],df['TotalPrice'])
#st.line_chart(a1)


# fig=plt.figure(figsize=(10,8))
# plt.plot(df['Year'],df['TotalPrice'])
# st.pyplot(fig)

# fig=plt.figure(figsize=(10,8))
# plt.bar(df['Year'],df['TotalPrice'])
# st.pyplot(fig)

if st.button('load bar chart'):
 df2=df.head(20)
 fig=plt.figure(figsize=(10,8))
 plt.bar(df2['Year'],df2['Qty'])
 st.pyplot(fig)
 
 
