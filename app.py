from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt

model = pickle.load(open("model.pkl", "rb"))


app = Flask(__name__)


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        first_day = float(request.form['first_day'])
        second_day = float(request.form['second_day'])
        third_day = float(request.form['third_day'])
        fourth_day = float(request.form['fourth_day'])
        fifth_day = float(request.form['fifth_day'])

        prediction = preprocessing.scale(
            np.array([[first_day], [second_day], [third_day], [fourth_day], [fifth_day]]))
        output = model.predict(prediction)

        output = np.around(output, 2)

        return render_template('index.html',
                               prediction_0="First day Stock value\n{}".format(
                                   output[0]),
                               prediction_1="Second day Stock value\n{}".format(
                                   output[1]),
                               prediction_2="Thrid day Stock value\n{}".format(
                                   output[2]),
                               prediction_3="Fourth day Stock value\n{}".format(
                                   output[3]),
                               prediction_4="Fifth day Stock value\n{}".format(
                                   output[4])
                               )


# @app.route("/plot", methods=['POST'])
# def lineplot():
#     if request.method == 'POST':
#         first_day = float(request.form['first_day'])
#         second_day = float(request.form['second_day'])
#         third_day = float(request.form['third_day'])
#         fourth_day = float(request.form['fourth_day'])
#         fifth_day = float(request.form['fifth_day'])

#         prediction = preprocessing.scale(
#             np.array([[first_day], [second_day], [third_day], [fourth_day], [fifth_day]]))
#         output = model.predict(prediction)

#         output_1 = np.around(output, 2)
#     sns.lineplot(data=output)
#     return render_template('plot.html', prediction_plot=plt.show())


if __name__ == "__main__":
    app.run(debug=True)
