import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO




st.title("LIDPlotter")
st.write(
    "This basic tool allows you to import a photometric data file (either IES or LDT), and from that file, extract overview information as well as a formatted polar intensity plot."
    )
st.divider()
st.subheader(
    "Photometric File Upload"
    )
uploaded_file = st.file_uploader(
    "Choose an IES or LDT file:",
    accept_multiple_files=False,
    type = ['IES', 'LDT']
    )

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)