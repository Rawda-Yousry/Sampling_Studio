# Sampling studio
## Table of contents

- [Overview](#Overview)
- [Features](#Features)
- [Application Demo](#application-demo)
- [Run the Project](#run-the-project)
- [Team Members](#team-23-members)

## Overview 
sampling studio is an educational website that enables the user to perform different functions on signals and can visualize it’s effects on signals instantly and all in one page.

## Features 
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
<p align="center">
 <img src=""/>
</p>


## Run the project
You need to install Python 3 and any python IDE on your computer.
- [Download Python 3](https://www.python.org/downloads/)
- [Download VS code](hhttps://code.visualstudio.com/download)

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
streamlit run FinalCode/signal_studio_app.py
```

## Team-23 Members

3rd Year Biomedical Engineering Students:

- [Amira Mohamed](https://github.com/AmeeraMOhammed)  Sec 1 - BN 15
- [Rawda Yousry](https://github.com/Rawda-Yousry) Sec 1 - BN 35
- [Doha Eid ](https://github.com/doha-eid)  Sec 1 - BN 49
- [Youssef Essam](https://github.com/jooo71)  Sec 2 - BN 58


