import streamlit as st
import pandas as pd
import mpld3
import streamlit.components.v1 as components
import csv
from io import StringIO
import numpy as np
import plotly.graph_objects as go

# fsample = st.slider("Fs",1,300)
t = np.linspace(0,3,900)

st.session_state.sig = pd.DataFrame({})
print(st.session_state.sig)
    

def readCsv(uploaded_file):
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        df =  pd.read_csv(uploaded_file)
        x = df.iloc[:,1]
        y = df.iloc[:,2]
        return x,y


def sampling(factor,freq,sin):
    samp_frq=factor* freq
    time_range=(t[-1]-t[0])
    samp_rate=int((len(t)/time_range)/((factor)*(freq)))
    samp_time=t[::samp_rate]
    samp_amp= sin[::samp_rate]
    return samp_time,samp_amp

def sinc_interp(factor,freq,sin):
    samp_time,samp_amp=sampling(factor,freq,sin)
    time_matrix= np.resize(t,(len(samp_time),len(t)))
    k= (time_matrix.T - samp_time)/(samp_time[1]-samp_time[0])
    resulted_matrix = samp_amp* np.sinc(k)
    reconstucted_seg = np.sum(resulted_matrix, axis=1)
    
    return  reconstucted_seg,samp_time,samp_amp

def noise(signal,snrRatio):
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

def save(signal):
    checkbox = st.checkbox("test button",key = "test_function", value = False)
    if checkbox:
        noised_signal = {"x-axis":t, "y-axis":signal }
        df= pd.DataFrame(noised_signal)
        # df.to_csv('noised signal.csv')
        # df = pd.DataFrame()
        st.session_state.sig = df
        print(st.session_state.sig)
        st.write(t)
        st.write(signal)


    @st.experimental_memo
    def convert_df(df):
        df.to_csv(index = False).encode('utf-8')

    st.download_button(
    "Press to Download",
    st.session_state.sig.to_csv(),
    "file.csv",
    "text/csv",
    key='download-csv'
    )
