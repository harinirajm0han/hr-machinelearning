import streamlit as st
import pandas as pd
st.title('🤖 Machine Learning App')

st.write('This is a machine leaarning app!')

df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df
