import matplotlib.pyplot as plt
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
from streamlit_option_menu import option_menu
from functions import *
st. set_page_config(layout="wide")
st.header('Generation signal')

global x,y
## plotting figure ##
mainSignal = px.line(height=450,width=1000)
noisedSignal= px.line(height = 350 ,width=1000)
changedSignal= px.line(height = 350 ,width=1000)
######## Side bar components #########
with st.sidebar:
    selected= option_menu(
        menu_title="Main Menu",
        options=["Home","Composer"],
        icons=["house","plus-circle-dotted"],
        menu_icon="cast",
        orientation="horizontal",
        
    )


    ## for uploading files ##
    
    ## for saving ##
    
    ## Add Noise ##

    # frequency = st.number_input('Frequency',1,90)
    # factor = st.number_input('Factor',1,90)
    # amplitude = st.number_input('Amplitude', 1,20)
    # addSignal = st.button("Add Signal")
    # drawAllSignal = st.button("Draw All Signals")
    


    # if addSignal:
    #     ADD_SIGNAL(frequency, amplitude)
    deleteList = []
    if len(Functions.ADDED_FREQUENCES) == 0:
        st.write('')
    else:
        for i in range(len(Functions.ADDED_FREQUENCES)):
            deleteList.append(f"amp = {Functions.ADDED_AMPLITUDES[i]} frequency ={Functions.ADDED_FREQUENCES[i]}")
        delList = st.multiselect("Signals to delete", deleteList)
        if st.button("Delete"):
            for i in range(len(delList)):
                if delList[i]:
                    DELETE_SIGNAL(i)
                    mainSignal.add_trace(go.Scatter(x=time,y=Functions.Current_amplitude))


    # sin = np.sin(2*np.pi*frequency*time)
    # mainSignal.add_trace(go.Scatter(x=time,y=Functions.Current_amplitude))


    
if selected =="Home":
    st.header(f" Welcome to our website") 
    st.write("Our website give you a lot of features to do on signal")
    st.write("Our website is designed for generation signal , plotting , sampling , adding nosie , reconstraction , add or remove signal ")
    st.write("The signal can come from loaded file or composer")


# if selected =="Add noise":
#     noiseCheckBox = st.checkbox("Add Noise")
#     snrRatio = st.number_input('SNR',1,260,1)
#     if noiseCheckBox:
#         noiseSignal=noise(Functions.Current_amplitude,snrRatio)
#         noisedSignal.add_trace(go.Scatter(x=time,y=noiseSignal),row=1,col=1)


if selected =="Composer":
    dataSet = st.selectbox("Which Type of signal you want?",("Loaded Signal","Uploaded Signal"))
    
    if dataSet == "Loaded Signal":
        frequency = st.number_input('Frequency',1,90)
        amplitude = st.number_input('Amplitude', 1,20)
        # factor = st.number_input('Factor',1,90)
        addSignal = st.button("Add Signal")
        sample = st.checkbox("Sampling")
        if addSignal:
            ADD_SIGNAL(frequency, amplitude)
        mainSignal.add_trace(go.Scatter(x=time,y=Functions.Current_amplitude))
        if sample:
            fsample = st.slider('Fs', 1,20)
            # freq = st.slider('Frequency',1,20)
            sampleTime,sampleAmp = sampling(fsample, time, Functions.Current_amplitude)
            changedSignal.add_trace(go.Scatter(x=sampleTime,y=sampleAmp))

    noiseCheckBox = st.checkbox("Add Noise")
    if noiseCheckBox:
        snrRatio = st.number_input('SNR',1,260,1)
        noiseSignal=noise(Functions.Current_amplitude,snrRatio)
        noisedSignal.add_trace(go.Scatter(x=time,y=noiseSignal),row=1,col=1)

    saveCheckBox = st.checkbox("Save File",key = "test_function", value = False)
    if saveCheckBox:
        save(Functions.Current_amplitude)

    if dataSet == "Uploaded Signal":
        uploaded_file = st.file_uploader("Upload your file")
        sample = st.checkbox("Sampling")

        if uploaded_file is not None:
            x,y = readCsv(uploaded_file)
            mainSignal.add_trace(go.Scatter(x=x,y=y))

        if sample:
            fsample = st.slider('Fs', 1,20)
            # freq = st.slider('Frequency',1,20)
            sampleTime,sampleAmp = sampling(fsample, time, Functions.Current_amplitude)
            changedSignal.add_trace(go.Scatter(x=sampleTime,y=sampleAmp))
            # drawNoiseOnCsv(x, y)
            # mainSignal.add_trace(go.Scatter(x=sampleTimePoints,y=sampleAmpPoints),row=1,col=1)
            # interpolatedSignal,sampleTimePoints,sampleAmpPoints = sinc_interp(factor,frequency,x,y)

        
        
    st.write(mainSignal)
    st.write(changedSignal)
    st.write(noisedSignal)



    

        





    

# interpolatedSignal,sampleTimePoints,sampleAmpPoints = sinc_interp(factor,frequency,time,Functions.Current_amplitude)



   
# if uploaded_file is not None:
#     x,y = readCsv(uploaded_file)
#     changedSignal.add_trace(go.Scatter(x=x,y=y),row=1,col=1)
#     # mainSignal.add_trace(go.Scatter(x=sampleTimePoints,y=sampleAmpPoints),row=1,col=1)
#     interpolatedSignal,sampleTimePoints,sampleAmpPoints = sinc_interp(factor,frequency,x,y)
    # mainSignal.add_trace(go.Scatter(x=x,y=interpolatedSignal),row=1,col=1)

# fig = px.line(x=t,y=interpolatedSignal)
# fig.add_trace(go.Scatter(x=t,y=sin),row=1,col=1)
# fig.add_trace(go.Scatter(x=sampleTimePoints,y=sampleAmpPoints),row=2,col=1)
# fig.add_trace(go.Scatter(x=t,y=interpolatedSignal),row=2,col=1)


# st.write(mainSignal)
# st.write(changedSignal)
# st.write(noisedSignal)
# st.write(fig)

# factor = st.sidebar.slider('factor',1,20,1,1)

# plt.subplot(212)
# plt.plot(x,y)

# fig_html = mpld3.fig_to_html(fig)
# components.html(fig_html, height=600)