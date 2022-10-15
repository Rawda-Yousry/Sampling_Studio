import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
import streamlit as st
import mpld3
import streamlit.components.v1 as components
# import numpy
import numpy as np
  
# define electrocardiogram as ecg model
ecg = electrocardiogram()

# frequency is 360
fs = st.slider('Sample Size', 330, 400,30)
frequency = 360
# n = np.arange(0, 0.5/ T) 

  
# calculating time data with ecg size along with frequency
time_data = np.arange(ecg.size) / frequency
time_data1 = np.arange(ecg.size) / fs

fig = plt.figure()
plt.subplot(211)
plt.plot(time_data, ecg,label='ECG Signal')
plt.xlabel('time', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')
plt.xlim(9, 10.2)
plt.ylim(-1, 1.5)

plt.subplot(212)
plt.plot(time_data1, ecg, 'ro', label='Sample marks after resampling at fs= ' + str(fs) +' Hz')
plt.plot(time_data1, ecg, 'g-', label='Reconstructed Sine Wave')
plt.xlabel("time in seconds")
plt.ylabel("ECG in milli Volts")
plt.legend(fontsize=10, loc='upper right')
plt.xlim(9, 10.2)
plt.ylim(-1, 1.5)
  
# plotting time and ecg model



fig_html = mpld3.fig_to_html(fig)

plt.tight_layout()

components.html(fig_html, height=600)
