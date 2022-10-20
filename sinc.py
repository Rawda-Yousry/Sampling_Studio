import tile
import numpy as np
import tile
from matplotlib import pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import mpld3

plt.subplots_adjust(bottom=0.109,right =0.7,left=0.05,
                    top=1)
                    
def sinc_interp(factor,fmax):
    plt.subplot(211)
    t = np.linspace(0,1,250)
    sin =np.sin(2*np.pi*fmax*t)
    # t_axis = np.linspace(0,0.5,len(y_axis))
    plt.plot(t,sin)
    samplingTime = np.arange(0,1,1/(factor*fmax))
    # if len(y_axis) != len(t_axis):
    #     raise (Exception,'t and y must be the same length')
    # Find the period    
    T = (t[1] - t[0])
    t = np.array(t)
    samplingTime = np.array(samplingTime)
    sincM = np.tile(samplingTime, (len(t), 1)) - np.tile(t[:, np.newaxis], (1, len(samplingTime)))
    yNew = np.dot(sin, np.sinc(sincM/T))
    plt.subplot(211)
    plt.plot(samplingTime,yNew,'r-')


frequency = st.slider("freq",1,20) 
factor = st.slider("Factor",1,20)
fig =plt.figure(figsize=(6,6))
plt.ylim(-1,1)

# print(t)
# u = np.linspace(-4,4,200)
# t = np.linspace(0,0.5,250)
# sinFunction = np.sin(2*np.pi*t*frequency)
# result = sinc_interp(t,factor,frequency)
sinc_interp(factor,frequency)
# plt.plot(t,sinFunction)
# plt.plot(t, result,'r')
fig_html = mpld3.fig_to_html(fig)

plt.tight_layout()

components.html(fig_html, height=800)

# s = [1,2,3,4]
# u = [2,3,4,6]
# s = np.array(s)
# u = np.array(u)
# print(np.tile(u, (len(s), 1)))

# print(np.tile(s[:, np.newaxis], (1, len(u))))
# sincM = np.tile(u, (len(s), 1)) - np.tile(s[:, np.newaxis], (1, len(u)))
# print(sincM)


