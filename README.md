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

## Application Demo


## Run the project
You need to install Python 3 and any python IDE on your computer.
* Download Python 3
* Download VS code
1- Clone repository
```
https://github.com/Rawda-Yousry/DSP_Task1_-Team23-

```
2- Prepare Requirements
```
pip install -r requirements.txt
```

3- Run the App
```
streamlit run signal_studio_app.py
```

