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

    parser = DataParser(string_data)
    parser.parse()

    "### Metadata"
    st.code(parser.metadata)

    st.dataframe(parser.df)

    # graph it
    fig, ax = plt.subplots()
    ax.plot(parser.df["Time"], parser.df["Altitude"])
    st.pyplot(fig)
    # parser.df
    # st.line_chart(data=parser.df[["Time", "Altitude"]])
    # st.line_chart(data=[parser.df["Time"], parser.df["Altitude"]])

    "### Full data"
    with st.expander("See full data"):
        st.code(string_data)
