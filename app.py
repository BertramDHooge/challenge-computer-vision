import os
from flask import Flask
from flask import request
from flask import render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
from skimage.filters import unsharp_mask
from PIL import Image
import cv2

app = Flask(__name__)
categories = ['Actinic keratoses', 'Basal cell carcinoma', 'Benign keratosis-like lesions ', 'Dermatofibroma', 'Melanocytic nevi', 'Melanoma', 'Vascular lesions']
UPLOAD_FOLDER = 'upload/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

model = load_model("./models/model")

def predict(img):
    temp_img = unsharp_mask(cv2.medianBlur(np.asarray((Image.open("static/" + img).resize((120,120)))),5))
    predictable_img = np.reshape(temp_img, [1, 120, 120, 3])
    return model.predict(predictable_img)

# add routes for the form, make a prediction template where we have the result and a back button
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html", title="Home")

    if request.method == "POST":
        data = request.files
        form_image = data.get("image")
        print(data)
        form_image.save(os.path.join("static", app.config['UPLOAD_FOLDER'], form_image.filename))
        print(form_image.filename)
        if form_image and allowed_file(form_image.filename):
            #print('upload_image filename: ' + filename)
            img = f"{UPLOAD_FOLDER}{form_image.filename}"
            return render_template('prediction.html', img=img, prediction=predict(img), categories=categories)




        return render_template("index.html")

if __name__ == "__main__":
   app.run()
