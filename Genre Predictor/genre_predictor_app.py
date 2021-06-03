
from flask import Flask, request
from flask import render_template, jsonify

from fastai.learner import load_learner
from fastai.vision.core import PILImage

from waitress import serve

import pickle
import os



app = Flask(__name__)


# include these methods for use by saved model
def get_x(r):
    return path + 'train_data/' + r['id'].astype(str) + '.jpg'

def get_y(r):
    return r['genres']


learn = load_learner('./model/single_label/single_genre_predictor_fastai.pkl')
classes = learn.dls.vocab



@app.route('/')
def main_page():
    return render_template('genre_predictor.html')


def predict_genre(img_file):
    # save image to display after prediction
    path = 'static/tmp'
    if not os.path.exists(path):
        os.mkdir(path)
    path = os.path.join(path, 'tmp.jpg')
    img_file.save(path)

    # get poster image and return prediction
    prediction = learn.predict(PILImage.create(img_file))
    predicted_genre = classes[prediction[1].item()]

    return render_template('predict.html', prediction=predicted_genre)


@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['poster']
    return predict_genre(file)

if __name__ == '__main__':
    #app.run(debug=True)
    serve(app, host='0.0.0.0', port=80)



# Reference: 
# 1. https://medium.com/usf-msds/creating-a-web-application-powered-by-a-fastai-model-d5ee560d5207
# 2. https://medium.com/@nutanbhogendrasharma/deploy-machine-learning-model-with-flask-on-heroku-cd079b692b1d