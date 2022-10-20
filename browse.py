import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import mpld3
import streamlit.components.v1 as components
import csv
from io import StringIO
from datetime import datetime
import numpy as np
from scipy.signal import resample


f = st.slider('Frequency', 50, 700, 25)
sampleRate = st.slider('Sample Frequency', 50, 700, 25)
uploaded_file = st.file_uploader( "UPLOAD signal file here")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    string_data = stringio.read()

    # fig= plt.figure(figsize=(9,6.5))
    # plt.subplots_adjust(bottom=0.109,right =0.7,left=0.05,
    #                 top=1)
    plt.subplots_adjust(bottom=0.109,right =0.7,left=0.05,
                    top=1)

# with open("uploaded_file.csv") as csvfile:
    fig = plt.figure()
    df =  pd.read_csv(uploaded_file)
    x = df.iloc[:,0]
    y = df.iloc[:,1]
    z= df.iloc[:,2]
    plt.subplot(211)
    # t= np.linspace(0,0.5,f)
    # yup = resample(y,f)
    plt.plot(x,y)
    def sinc_interp(factor,fmax,x,y):
        # t_axis = np.linspace(0,0.5,len(y_axis))
        samplingTime = np.arange(0,1.1,1/(factor*fmax))
        # if len(y_axis) != len(t_axis):
        #     raise (Exception,'t and y must be the same length')
        # Find the period
        x = np.array(x)    
        T = (x[1] - x[0])
        # t_axis = np.array(t_axis)
        # samplingTime = np.array(samplingTime)
        sincM = np.tile(samplingTime, (len(x), 1)) - np.tile(x[:, np.newaxis], (1, len(samplingTime)))
        yNew = np.dot(y, np.sinc(sincM/T))
        plt.subplot(211)
        plt.plot(samplingTime,yNew,'ro')
    

    # tup = np.linspace(0,0.5,sampleRate)
    # y1 = resample(y,sampleRate)
    # # y1 = resample(y,sampleRate)
    
    # plt.plot(tup,y1)
    
    frequency = st.slider("freq",1,300) 
    factor = st.slider("Factor",1,300)
    sinc_interp(factor, frequency, x, z)


    fig_html = mpld3.fig_to_html(fig)
    components.html(fig_html, height=600)




# df = pd.read_csv('data.csv')

# df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%Y %H:%M')

# x = df['DATE']
# y = df['Sensor Value']

# plt.plot(x,y)
# # beautify the x-labels
# plt.gcf().autofmt_xdate()

# plt.show()



    # count = 0 #df = pd.read_csv("input.csv", usecols=columns)
    # arr1 = []   dataset = pd.read_csv('data.csv')
    # arr2 = []
    
    # fig = plt.figure() 
    # for row in reader:
    #     arr1.append(row[0])
    #     arr2.append(row[1])
    #     if count > 10:
    #         break
    # arr1.remove(arr1[0])
    # arr2.remove(arr2[0])
    # arr1Up = [float(x) for x in arr1]
    # arr2Up = [float(x) for x in arr2]
    # plt.plot(arr1Up,arr2Up)

    # st.pyplot(fig) 