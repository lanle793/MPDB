
from flask import Flask, request
from flask import render_template, jsonify
from fastai.learner import load_learner
from fastai.vision.core import load_image
import pickle
import datetime


app = Flask(__name__)


learn = load_learner('./model/single_label/single_genre_predictor_fastai.pkl')
classes = learn.data.classes


@app.route('/')
def main_page():
    return render_template('genre_predictor.html')

def predict_genre(img_file):
    # get poster image and return prediction
    prediction = learn.predict(load_image(img_file))
    predicted_genre = classes[prediction[1].item()]

    response = {
        'status': 200,
        'prediction': predicted_genre,
        'created_at': datetime.datetime.now()
    }

    return response

@app.route('/predict', method=['POST'])
def predict():
    return jsonify(predict_genre(request.files['image']))

if __name__ == '__main__':
    app.run()



# Reference: https://medium.com/usf-msds/creating-a-web-application-powered-by-a-fastai-model-d5ee560d5207