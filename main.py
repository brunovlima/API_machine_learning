import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


file = open('irishtopickle.pkl', 'rb')
model = pickle.load(file)


@app.route("/", methods=['POST', 'GET'])
def entry_point():
    if request.method == "POST":
        dict = request.form
        Sepal_length = float(dict['Sepal_length'])
        Sepal_width = float(dict['Sepal_width'])
        Petal_length = float(dict['Petal_length'])
        Petal_width = float(dict['Petal_width'])
        input = [Sepal_length, Sepal_width, Petal_length, Petal_width]
        predict = model.predict([input])
        print(predict)

        return render_template('resultado.html', dict=dict, predict=predict)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
