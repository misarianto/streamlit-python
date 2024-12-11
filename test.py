import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Streamlit Demos')

st.write('Welcome to the Streamlit demos app!')

st.header('Interactivity with Widgets')

name = st.text_input('Enter your name')
st.write(f'Hello, {name}!')

age = st.number_input('Enter your age', min_value=0, max_value=120, value=18)
st.write(f'You are {age} years old')

slider = st.slider('Select your slider level', min_value=1, max_value=10, value=5)
st.write(f'Slider: {slider}')

if st.button('Say Hello!'):
    st.write('Hello YouTube!')

option = st.selectbox('Choose on option:', [1,2,3])
st.write(f'You select: {option}')

st.header('Displaying Data and Charts')

data = {
    'Name': ['Alince', 'Bob', 'Charline'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)
st.subheader('Sample DataFrame')
st.write(df)

st.subheader('Matplotlib Chart')
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x))
st.pyplot(fig)

st.subheader('Columns Layout')
col1, col2 = st.columns(2)

with col1:
    st.write('Content for col1')
with col2:
    st.write('Content for col2')


st.subheader('Tab Layout')
tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
with tab1:
    st.write('Content for tab1')
with tab2:
    st.write('Content for tab2')

st.subheader('Sidebar Title')
sidebar_option = st.sidebar.selectbox('Select an option', ['A', 'B', 'C'])
st.sidebar.write(f'You selected: {sidebar_option}')