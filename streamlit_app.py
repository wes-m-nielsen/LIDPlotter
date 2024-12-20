import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib as plt
from io import StringIO

st.image("FOS-Logo.png", width = 200)
st.title("LIDPlotter")
st.write(
    "This basic tool allows you to import a photometric data file (either IES or LDT), and from that file, extract some overview photometric details as well as produce a formatted polar intensity plot."
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

if st.button("Evaluate"):
    st.write("Orright then, here ya go")

    if uploaded_file is not None:
        # To convert to a string based IO:
        file = StringIO(uploaded_file.getvalue().decode("utf-8"))
        #st.write(stringio)

        metadata = {}
        angles = []
        intensities = []

        lines = file.readlines()

        # Remove any empty lines
        lines = [line.strip() for line in lines if line.strip()]
        
        # Identify file type
        file_ext = uploaded_file[-3:].lower()
        
        # Start parsing the IES file
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Parse the header
            if line.startswith("IESNA"):
                metadata['standard'] = line  # E.g., IESNA-IES:1990
                i += 1
                continue
            
            # Parse the metadata section
            if line.startswith("MANUFACTURER"):
                metadata['manufacturer'] = line.split(":", 1)[1].strip()
            elif line.startswith("LUMINAIRE"):
                metadata['luminaire'] = line.split(":", 1)[1].strip()
            elif line.startswith("CATALOG"):
                metadata['catalog_number'] = line.split(":", 1)[1].strip()
            elif line.startswith("TEST"):
                metadata['test'] = line.split(":", 1)[1].strip()

            # Identify the start of the data section
            if line.startswith("TILT"):
                i += 1
                break

            i += 1

        # Parsing data section (angles and intensities)
        while i < len(lines):
            line = lines[i]
            
            # Skip over metadata lines
            if line.startswith("TILT"):
                i += 1
                continue
            
            # Extract angles and intensities
            values = line.split()
            if len(values) > 1:
                angles.append(float(values[0]))  # Angle in degrees
                intensities.append(float(values[1]))  # Intensity value (candela)

            i += 1
        
        # Create a DataFrame
        data = pd.DataFrame({'Angle': angles, 'Intensity': intensities})
        
        st.write(data)

    
        #st.dataframe(data)
        #st.write(metadata['manufacturer'])

    else: st.write("Hang on... no file loaded yet, you numbskull!!!")