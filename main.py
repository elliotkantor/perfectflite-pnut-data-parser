import streamlit as st
from parse import DataParser
import matplotlib.pyplot as plt
from io import StringIO


st.title("Pnut Altimeter Data Parser")

file = st.file_uploader("Upload your pf2 file", ("pf2"))


if file:
    # get string from file
    string_data = StringIO(file.getvalue().decode("utf-8")).read()

    Parser = DataParser(string_data)
    Parser.parse()

    "### Time vs Altitude Graph"
    fig, ax = plt.subplots()
    ax.plot(Parser.df["Time"], Parser.df["Altitude"])
    st.pyplot(fig)

    left, right = st.columns([1, 1.5])

    with left:
        st.metric("Apogee", f"{Parser.apogee} feet")
        "### Metadata"
        st.code(Parser.metadata)

    with right:
        st.metric("Flight number", Parser.flight_number)
        "### Flight data"
        st.dataframe(Parser.df)
        st.download_button(
            "Download data spreadsheet",
            Parser.df.to_csv(line_terminator="\r\n", index=False),
            file_name="data.csv",
            on_click=st.balloons,
        )

    "### Full data"
    with st.expander("See full data"):
        st.code(string_data)
