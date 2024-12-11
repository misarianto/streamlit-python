import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Financial Portofolio Analysis Tool')

principle = st.number_input('Inital Investment Amount', min_value=0.0, value=1000.0, step=100.0)
annual_interest_rate = st.number_input('Annual Interest Rate (%)', min_value=0.0, value=5.0, step=0.1)
years = st.number_input('Number of years', min_value=1, value=10, step=1)

interest_rate = annual_interest_rate / 100
time = np.arange(1, years + 1)
amount = principle * (1+interest_rate) ** time

data = pd.DataFrame({
    'Year': time,
    'Investment Value': amount.round(2)
})

st.subheader('Investment growth over time')
st.dataframe(data)

fig, ax = plt.subplots()
ax.plot(data['Year'], data['Investment Value'], marker='o')
ax.set_xlabel('Year')
ax.set_ylabel('Investment Value')
ax.set_title('Investment growth over time')
ax.grid(True)

st.pyplot(fig)