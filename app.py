from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('pickle_dump2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    input_1 = [int(x) for x in request.form.values()]
    print(input_1)
    output_1 = model.predict([input_1])
    return render_template('index.html', prediction_text='Rent of home you are looking for is {}Rs per month'.format(output_1))

if __name__ == "__main__":
    app.run(debug=True)
