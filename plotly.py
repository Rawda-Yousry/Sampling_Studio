import numpy as np
# import plotly.express as px
# import plotly.graph_objs as go
import streamlit as st
from scipy import signal
from matplotlib import pyplot as plt
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import mpld3
from scipy.signal import resample



sampleRate = st.sidebar.slider('Sample Frequency', 1, 200, 25)
frequency_of_signal = st.sidebar.slider('Original Frequency',1, 200, 25)
amp = st.sidebar.slider('Amplitude',1,200,1)
t = np.linspace(0, 1, 500) #time steps
signal = amp * np.sin(2 * np.pi * frequency_of_signal * t) # sine wave  
fig= plt.figure(figsize=(12,6))
plt.subplots_adjust(bottom=0.2,right =0.5,left=0.06,top=0.9)


    
    # st.pyplot(fig)

def addSignal():
    time = np.linspace(0, 1, 200)
    addedSignal = np.sin(3*2*np.pi*frequency_of_signal*t)+ 3 * np.cos(3*2*np.pi*frequency_of_signal*time)
    plt.plot(211)
    draw(time,addedSignal,'SineWave of frequency' + str(frequency_of_signal),15,'time','Amplitude','upper right')


def noise(signal):
    snrRatio = st.sidebar.slider('SNR',1,20,1)
    power = signal**2
    snr_db = 10 * np.log10(snrRatio)
    signal_avg_power=np.mean(power)
    signal_avg_power_db=10 * np.log10(signal_avg_power)
    noise_db=signal_avg_power_db - snr_db
    noise_watts=10 ** (noise_db/10)
    mean_noise=0
    noise=np.random.normal(mean_noise, np.sqrt(noise_watts),len(signal))
    noise_signal = signal+noise
    return noise_signal


def draw(x,y,label,fontsize,xlabel,ylabel,loc):
    plt.plot(x,y,label = str(label))
    plt.xlabel(xlabel,fontsize = int(fontsize))
    plt.ylabel(ylabel,fontsize = int(fontsize))
    plt.legend(fontsize=int(10), loc=str(loc))
    plt.ylim(-8,10)

def drawSample(y,shape,label,fontsize,xlabel,ylabel,loc):
    t = np.linspace(0,0.5,sampleRate)
    y = resample(y,sampleRate)
    plt.xlabel(xlabel,fontsize = int(fontsize))
    plt.ylabel(ylabel,fontsize = int(fontsize))
    plt.plot(t,y,str(shape), label=str(label))
    plt.legend(fontsize=int(10), loc = str(loc))
    plt.ylim(-8,10)



def noise_return():
    signalWithNoise=noise(signal)
    draw(t,signalWithNoise,'SineWave of frequency' + str(frequency_of_signal),15,'time','Amplitude','upper right')





# def denoise():
#     noise = 0


plt.subplot(211)
#draw(t,signal,'SineWave of frequency' + str(frequency_of_signal),15,'time','Amplitude','upper right')
# addSignal()
signalWithNoise=noise(signal)
draw(t,signalWithNoise,'SineWave of frequency' + str(frequency_of_signal),15,'time','Amplitude','upper right')

plt.subplot(212)
drawSample(signal, 'ro', 'Sample marks after resampling at fs =' +str(sampleRate) +'Hz' ,10,'time','Amplitude','upper right')
drawSample(signal, 'g-','Reconstructed Sine Wave',10,'time','Amplitude','upper right')

st.pyplot(fig = fig)
    
fig_html = mpld3.fig_to_html(fig)

plt.tight_layout()

components.html(fig_html, height=800)




