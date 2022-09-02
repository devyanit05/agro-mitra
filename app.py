from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)

# to load model from crop-prediction file these first two lines are added
path = '/Users/mohd.ashharullah/Documents/Agro/crop-prediction'
pickle_fn = path + '/' + 'model.pkl'
model = pickle.load(open(pickle_fn, 'rb'))


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/info', methods=['GET'])
def info():
    return render_template('info.html')


# @app.route('/predict', methods=['GET'])
# def predict():
#     return render_template('prediction.html')


@app.route('/detect', methods=['GET'])
def detect():
    return render_template('disease.html')


@app.route('/predict', methods=['GET', 'POST'])
def Home():
    pred = False
    if request.method == 'POST':
        dataN = request.form['Nitrogen']
        dataP = request.form['Phosphorus']
        dataK = request.form['Potassium']
        dataM = request.form['Moisture']
        dataR = request.form['rain']
        dataT = request.form['Temp']
        datapH = request.form['ph']
        arr_data = np.array(
            [[dataN, dataP, dataK, dataM, dataR, dataT, datapH]])
        # print(dataN,dataP, dataK, dataM, dataR, dataT, datapH)
        pred = (model.predict(arr_data))
        pred[0] = pred[0].upper()
        print(pred, pred[0])

    return render_template('prediction.html', pred=pred)


if (__name__ == "__main__"):
    app.run(debug=True, port=5001)
