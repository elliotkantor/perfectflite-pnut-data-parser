import streamlit as st
import pandas as pd
from parse import DataParser
import matplotlib.pyplot as plt

st.title("Pnut Altimeter Data Parser")
file = st.file_uploader("Upload your pf2 file")

parser = DataParser(file)
parser.parse()
df = parser.get_dataframe()

# graph it
plt.plot(df.Time, df.Altitude)