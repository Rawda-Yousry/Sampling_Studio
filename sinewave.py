import numpy as np
import plotly.graph_objects as go
import streamlit as st
from scipy import signal
from matplotlib import pyplot as plt
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import mpld3

with st.sidebar:
    selected = option_menu(
        menu_title ="main menu",
        options =['New','Edit']
    )

sampleRate = st.slider('Sample Size', 0, 200, 25)

f = 20 # freq (Hz)
t = np.linspace(0, 0.5, 200) #time steps
x1 = np.sin(2 * np.pi * f * t) # sine wave 
s_rate = sampleRate # Hz. Here the sampling frequency is less than the requirement of sampling theorem


T = 1 / s_rate 
n = np.arange(0, 0.5/ T) 
nT = n * T
x2 = np.sin(2 * np.pi * f * nT) # Since for sampling t = nT.
fig= plt.figure(figsize=(9,5))
plt.subplots_adjust(bottom=0.1,
                    top=1)


plt.subplot(211)
plt.plot(t, x1,label='SineWave of frequency ' + str(f))
plt.xlabel('time', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(212)
plt.plot(nT, x2, 'ro', label='Sample marks after resampling at fs= ' + str(sampleRate*nT[-1]) +' Hz')
plt.plot(nT, x2, 'g-', label='Reconstructed Sine Wave')
plt.legend(fontsize=10, loc='upper right')

plt.xlabel('time', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')
fig_html = mpld3.fig_to_html(fig)

plt.tight_layout()

components.html(fig_html, height=600)


