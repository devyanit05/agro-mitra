from flask import Flask,render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def Hello():
    return render_template('prediction.html')

@app.route('/predict', methods = ['POST'])
def Home():
    dataN = request.form['Nitrogen']
    dataP = request.form['Phosphorus']
    dataK = request.form['Potassium']
    dataM = request.form['Moisture']
    dataR = request.form['rain']
    dataT = request.form['Temp']
    datapH= request.form['ph']
    data = np.array([[dataN,dataP, dataK, dataM, dataR, dataT, datapH]])
    # print(dataN,dataP, dataK, dataM, dataR, dataT, datapH)
    pred = model.predict(data)
    print(pred)
    return render_template('soilPred.html')

if(__name__ == "__main__"):
    app.run(debug = True, port=5001)