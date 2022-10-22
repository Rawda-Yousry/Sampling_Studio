import matplotlib.pyplot as plt
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
from functions import *
from streamlit_option_menu import option_menu

st. set_page_config(layout="wide")

st.header('Generation signal')
with st.sidebar:
    selected= option_menu(
        menu_title="Main Menu",
        options=["Home","Composer","Add noise"],
        icons=["house","plus-circle-dotted","soundwave"],
        menu_icon="cast"
        
    )
    uploaded_file=st.sidebar.file_uploader("upload your file")
if selected =="Home":
    st.title(f"you have selected {selected}")

# uploaded_file=st.sidebar.file_uploader("uploade your flie")

# fsample = st.slider("Fs",1,300)
freq = st.sidebar.slider('Frequency',1,20,1,1)
sin = np.sin(2*np.pi*t*freq)
check = st.checkbox("Add Noise")
fig = make_subplots(rows=2, cols=1)
# fig.add_trace(go.Scatter(x=t,y=sin),row=1,col=1)

if check:
    snrRatio = st.slider('SNR',1,260,1)
    checked_noise=noise(sin,snrRatio)
    fig.add_trace(go.Scatter(x=t,y=checked_noise),row=2,col=1)
    st.write(fig)
    
save(sin)
x,y = readCsv(uploaded_file)
fig.add_trace(go.Scatter(x=x,y=y),row=1,col=1)
st.write(fig)

# interpolatedSignal,sampleTimePoints,sampleAmpPoints = sinc_interp(factor,freq,sin)


# fig.add_trace(go.Scatter(x=sampleTimePoints,y=sampleAmpPoints),row=2,col=1)
# fig.add_trace(go.Scatter(x=t,y=interpolatedSignal),row=2,col=1)

# fig = px.line(x=t,y=interpolatedSignal,range_x=[0,3],range_y=[-1,1])
# st.write(fig)

# factor = st.sidebar.slider('factor',1,20,1,1)

# plt.subplot(212)
# plt.plot(x,y)

# fig_html = mpld3.fig_to_html(fig)
# components.html(fig_html, height=600)