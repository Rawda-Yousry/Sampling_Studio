import tile
import numpy as np
import tile
from matplotlib import pyplot as plt
import streamlit as st
# from scipy import resample
import streamlit.components.v1 as components
import mpld3

plt.subplots_adjust(bottom=0.109,right =0.7,left=0.05,
                    top=1)
                    
def sinc_interp(factor,fmax):
    plt.subplot(211)
    t = np.linspace(0,1,200)
    t = np.array(t)
    sin =np.sin(2*np.pi*fmax*t)
    plt.plot(t,sin)
    samplingTime = np.arange(0,1.02,1/(factor))  
    T = (t[2] - t[1])
    t = np.array(t)
    samplingTime = np.array(samplingTime)
    sincM = np.tile(samplingTime, (len(t), 1)) - np.tile(t[:, np.newaxis], (1, len(samplingTime)))
    yNew = np.dot(sin, np.sinc(sincM/T))
    plt.subplot(211)
    plt.plot(samplingTime,yNew)
    plt.plot(samplingTime,yNew,'go')


frequency = st.slider("freq",1,40) 
fsample = st.slider("Fs",1,60)
fig =plt.figure(figsize=(6,6))
plt.ylim(-2,2)

# print(t)
# u = np.linspace(-4,4,200)
# t = np.linspace(0,0.5,250)
# sinFunction = np.sin(2*np.pi*t*frequency)
# result = sinc_interp(t,factor,frequency)
sinc_interp(fsample,frequency)
# plt.plot(t,sinFunction)
# plt.plot(t, result,'r')
fig_html = mpld3.fig_to_html(fig)

plt.tight_layout()

components.html(fig_html, height=800)


