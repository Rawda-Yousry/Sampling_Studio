# from os import PRIO_PGRP
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import mpld3
import streamlit.components.v1 as components
from matplotlib.image import imread


if 'index' not in st.session_state:
    st.session_state.index = 0

length=0

# time = np.linspace(0, 1, 200)

amp = st.slider("Enter your signal amplitude", step=1)
freq = st.slider("Enter your signal frequency", step = 1)
fig= plt.figure()

# sin = amp * np.sin(2*np.pi*freq*time)
# st.session_state.add_sig.append(sin)

if 'add_sig' not in st.session_state:
    st.session_state.add_sig = []

time = np.linspace(0, 1, 200)

if st.button("ADD"):
    time = np.linspace(0, 1, 200)
    st.session_state.add_sig.append(amp*np.sin(2 * np.pi * freq * time))
    st.session_state.index +=1


    

for index in range (0,len(st.session_state.add_sig)):
    plt.subplot(211)
    plt.plot(time,st.session_state.add_sig[index])


for index in range (0,len(st.session_state.add_sig)):
    print(index)
    length= length - st.session_state.add_sig[index]
    plt.subplot(212)
    plt.plot(time,length)

    

    
number=st.slider("index of removed signal")

if st.button("Remove"):
    if number == index:
        del st.session_state.add_sig[number]
    else :
        st.text("Out of range")
    

for index in range (0,len(st.session_state.add_sig)):
    plt.subplot(211)
    plt.plot(time,st.session_state.add_sig[index])


for index in range (0,len(st.session_state.add_sig)):
    print(index)
    length= length - st.session_state.add_sig[index]






fig_html = mpld3.fig_to_html(fig)
plt.tight_layout()
components.html(fig_html, height=600)