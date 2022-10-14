import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import csv

with open('static/test.csv') as csvfile:
    reader = csv.reader(csvfile)
    count = 0 
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






