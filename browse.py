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
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)
    # st.write(uploaded_file)

# str_filename = 'uploaded_file.csv'
# fh = dataframe = pd.read_csv(uploaded_file)
# csv_reader = csv.reader(fh)
# csv_header = next(csv_reader)
# lst_dt_csv = next (csv_reader)
# dt_csv = np.array(list(map(datetime.fromisoformat,lst_dt_csv[1:3])))
# lst_fs = next(csv_reader)
# np_d_fs = np.array(list(map(float,lst_fs[1:3])))
# fh.close()
# df_sig = pd.read_csv(uploaded_file, header = None, skiprows = 5, names = csv_reader)
# st.pyplot.df_sig
# st.pyplot.xlabel('sample number')
# st.pyplot.ylabel('signal value, volts')



# with open("uploaded_file.csv") as csvfile:
    fig,ax = plt.subplots()
    df =  pd.read_csv(uploaded_file)
    x = df.iloc[:,0]
    y = df.iloc[:,1]
    ax.plot(x,y)
    st.pyplot(fig = fig)




   

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
    # fig_html = mpld3.fig_to_html(fig)
    # components.html(fig_html, height=600)
    # st.pyplot(fig) 
