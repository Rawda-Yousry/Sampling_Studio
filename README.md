# Sampling studio

## Description 
sampling studio is an educational website that enables the user to perform different functions on signals and can visualize it’s effects on signals instantly and all in one page.

## Features and options 
* Changing signal frequency by a frequency slider that ranges from 1 to 90 HZ.
* Changing signal ampitude by amplitude slider that ranges from 1 to 20 .
* Generating basic sinusoidal wave and changing it’s frequency and amplitude.
* Sampling loaded sinusoidal wave and changing the sampling rate from 1 to 20 sample/wave.
* Reconstructing or recovering the original signal from the sampling points.
* Adding noise to signals by different SNR (signal to noise ratio) by a slider that ranges from 1 to 260.
* Adding many signals just by entering the desired frequency and ampitude of the signal to be added via sliders then clicking the add button then, sampling the resulted signal or applying noise to it.
* Deleting any of the added signals by simply select the signal that you want to delete from a multi-select and click the delete button.
* One graph to show original signal, sampling, noised signal and added signals.
* Uploading signal CSV file then editing these signal by changing frequency, amplitude or adding noise.
* Sampling the uploaded signal.
* Downloading the signals files after you finish editing it.

## Webpage


## Required libraries
* matplotlib library 3.6.0
* plotly library 5.10.0
* pandas library 1.5.1
* streamlit library 1.13.0
* csv library 3.10.8
* numpy library 1.23.4
* StringIO library 2.7.2.
* math library 3.10.8
* mpld3 

## Run the application 
In the terminal write the following command "Streamlit run signal_studio_app.py"

## Requirments 
$ pip install streamlit 
* pip install plotly
* pip install plotly.express
* pip install mpld3
* pip install matplotlib
* pip install pandas 
