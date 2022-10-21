import tile
import numpy as np
import tile
import math
from matplotlib import pyplot as plt
import streamlit as st
# from scipy import resample
import streamlit.components.v1 as components
import mpld3

plt.subplots_adjust(bottom=0.109,right =0.7,left=0.05,
                    top=1)

fig =plt.figure(figsize=(6,6))
plt.ylim(-1,1)
                    
freq = st.slider('Frequency',1,20,1,1)
factor = st.slider('factor',1,20,1,1)
plt.subplot(211)
plt.ylim(-1,1)

t = np.arange(0,2,2/1000)
sin = np.sin(2*np.pi*t*freq)
plt.plot(t,sin)

def sampling(factor):
    samp_frq=factor* freq
    time_range=(t[-1]-t[0])
    st.write(time_range)
    
    samp_rate=int((len(t)/time_range)/((factor)*freq))
    samp_time=t[::samp_rate]
    # samp_time = np.array(samp_time)
    # samp_time.remove(samp_time[0])
    st.write(samp_time)
    samp_amp= sin[::samp_rate]
    return samp_time,samp_amp

def sinc_interp(factor):
    samp_time,samp_amp=sampling(factor)
    time_matrix= np.resize(t,(len(samp_time),len(t)))
    k= (time_matrix.T - samp_time)/(samp_time[1]-samp_time[0])
    resulted_matrix = samp_amp* np.sinc(k)
    reconstucted_seg= np.sum(resulted_matrix, axis=1)
    
    return  reconstucted_seg,samp_time,samp_amp
    
interpolatedSignal,sampleTimePoints,sampleAmpPoints = sinc_interp(factor)
plt.subplot(212)
plt.ylim(-1,1)
plt.plot(t,interpolatedSignal)
# plt.plot(sampleTimePoints,sampleAmpPoints,'go')

# def sinc_interp(factor,fmax):
#     plt.subplot(211)
#     t = np.linspace(0,1,200)
#     t = np.array(t)
#     sin =np.sin(2*np.pi*fmax*t)
#     plt.plot(t,sin)
#     samplingTime = np.arange(0,1,1/(factor))  
#     T = (t[2] - t[1])
#     t = np.array(t)
#     samplingTime = np.array(samplingTime)
#     sincM = np.tile(samplingTime, (len(t), 1)) - np.tile(t[:, np.newaxis], (1, len(samplingTime)))
#     yNew = np.dot(sin, np.sinc(sincM/T))
#     plt.subplot(211)
#     plt.plot(samplingTime,yNew)
#     plt.plot(samplingTime,yNew,'go')


# frequency = st.slider("freq",1,40) 
# fsample = st.slider("Fs",1,60)


# print(t)
# u = np.linspace(-4,4,200)
# t = np.linspace(0,0.5,250)
# sinFunction = np.sin(2*np.pi*t*frequency)
# result = sinc_interp(t,factor,frequency)
# sinc_interp(fsample,frequency)
# plt.plot(t,sinFunction)
# plt.plot(t, result,'r')
fig_html = mpld3.fig_to_html(fig)

plt.tight_layout()

components.html(fig_html, height=800)


