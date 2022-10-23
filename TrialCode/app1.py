import streamlit as st
import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import csv

with open('static/test.csv') as csvfile:
    reader = csv.reader(csvfile) 
    arr1 = []
    arr2 = []
    for row in reader:
        arr1.append(row[0])
        arr2.append(row[1])    
    arr1Up = [float(x) for x in arr1]
    arr2Up = [float(x) for x in arr2]
    st.title('ECG signal')
    fig = plt.figure()
    plt.xlim([0,1])
    plt.xlabel("time")
    plt.ylabel("yaxis")
    plt.ylim([-1,2])
    plt.plot(arr1Up,arr2Up)
    fig_html = mpld3.fig_to_html(fig)
    components.html(fig_html, height=600)
    
    st.pyplot(fig)







