from flask import Flask, render_template,request,redirect,url_for
import os
import pandas as pd
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        file = request.files['csvfile']
        if not os.path.isdir('static'):
            os.mkdir('static')
        filepath = os.path.join('static',file.filename)
        file.save(filepath)
        return redirect(url_for('dash'))
    return render_template('home.html')


@app.route('/dash',methods=['GET','POST'])
def dash():
    if request.method == 'POST':
        variable1 = request.form['variable1']
        variable2 = request.form['variable2']
        data = pd.read_csv('static/test.csv')
        x = data[variable1]
        y = data[variable2]
        plt.plot(x,y)
        imagepath = os.path.join('static','image' + '.png')
        plt.savefig(imagepath)
        return render_template('image.html',image = imagepath)
    return render_template('dash.html')
    



if __name__ =="__main__":
    app.run(debug=True)




