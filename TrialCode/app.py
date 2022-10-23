import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import mpld3
import streamlit.components.v1 as components
import csv
from io import StringIO



uploaded_file = st.file_uploader( "UPLOAD signal file here")
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

    reader =  pd.read_csv(uploaded_file)
    count = 0 #df = pd.read_csv("input.csv", usecols=columns)
    arr1 = []
    arr2 = []
    
    fig = plt.figure() 
    for row in reader:
        arr1.append(row[0])
        arr2.append(row[1])
        if count > 10:
            break
    arr1.remove(arr1[0])
    arr2.remove(arr2[0])
    arr1Up = [float(x) for x in arr1]
    arr2Up = [float(x) for x in arr2]
    plt.plot(arr1Up,arr2Up)
    fig_html = mpld3.fig_to_html(fig)
    components.html(fig_html, height=600)
    st.pyplot(fig)