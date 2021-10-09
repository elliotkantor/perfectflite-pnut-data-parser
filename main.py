import streamlit as st
import pandas as pd
from parse import DataParser
import matplotlib.pyplot as plt
from io import StringIO


st.title("Pnut Altimeter Data Parser")

file = st.file_uploader("Upload your pf2 file", ("pf2"))

if file:
    # get string from file
    string_data = StringIO(file.getvalue().decode("utf-8")).read()
    st.code(string_data)

    # parser = DataParser(string_data)
    # parser.parse()
    # df = parser.get_dataframe()

    # # graph it
    # st.line_chart(data=df["Time", "Altitude"])
