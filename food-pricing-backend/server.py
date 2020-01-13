# TUTORIAL: https://codefresh.io/docker-tutorial/hello-whale-getting-started-docker-flask/

import picamera
import time
import pyrebase
import uuid
import glob
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications import imagenet_utils
from flask import Flask, send_file
from pyrebase_utils import db # If an error occurs in this line, delete it.

app = Flask(__name__)

model = load_model("model.hdf5")
dirpathSecrets = os.getcwd() + "/firebase_secrets.json"
path = '/home/pi/backend/food-pricing-backend/data/*.jpg'
jpg = '.jpg'

config = {
    'apiKey': 'AIzaSyCCL8LNWfr2Ri2wSOV8rjlbxZ4S1SWRWco',
    'authDomain': 'tum-food-app.firebaseapp.com',
    'databaseURL': 'https://tum-food-app.firebaseio.com',
    'storageBucket': 'tum-food-app.appspot.com',
    'serviceAccount': dirpathSecrets
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()


# feature enginnering
def create_features(dataset):
     x_scratch = []
     for imagePath in dataset:
         image = load_img(imagePath, target_size=(224, 224))
         image = img_to_array(image)
         image = np.expand_dims(image, axis=0)
         image = imagenet_utils.preprocess_input(image)
         x_scratch.append(image)
         x = np.vstack(x_scratch)
     return x

@app.route('/')
def mainRoute():
    return 'Hello!'

@app.route('/predict', methods=['GET']) # you can delete methods=['GET'] if this line return an error
def predict():
    id = str(uuid.uuid4())
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)
        camera.start_preview()
        time.sleep(1)
        camera.capture('/home/pi/backend/food-pricing-backend/data/%s%s' %(id,jpg) )

        storage.child("/predictions/%s%s" %(id,jpg)).put("/home/pi/backend/food-pricing-backend/data/*.jpg")

# # loding the ml model 
    categories = ['Bread','Dairy product','Dessert','Egg','Fried food','Meat','Noodles/Pasta','Rice','Seafood', 'Soup', 'Vegetable/Fruit']
    picture_image = glob.glob(path)
    picture_features = create_features(picture_image)
    prediction = model.predict(picture_features)
    os.remove("/home/pi/backend/food-pricing-backend/data/%s%s" %(id,jpg) )

## under this is the code which sends the json to the firebase. This code is under testing. They might return you an error.

## three types of errors might occure. The first one is syntax error. For this error, there are two possible reasons. 
## the first reason is purely, syntax error in line 80. The second one is the library (pyrebase) is not maintained properly and
## therefor, the unknown reason of syntax error occurs. read (https://stackoverflow.com/questions/57333606/unknown-syntax-error-on-calling-pyrebase-in-python)
## the alternative is to use another library (python-firebase) which @tech-ken don't know if it works properly or not due to that never used it before.

## line 78 might return an error also due to syntax error, but this is more a python syntax issue.

    label = categories[np.argmax(prediction)
    data = {"id": "%s%s" %(id.jpg), "label": "%s" %(label), "wieght": "10", "price": "20", "iscorrect": "false"}
    db.child("/predictions").push(data)
    
## for debugging perpose. comment out line 79 ~ 81 and activate line 84 and 85 to check if pyrebase for database works properly or not.
## documents in (https://github.com/thisbejim/Pyrebase)
                       
#     fake = {"id": "a", "label": "b"}
#     db.child("/predictions").push(fake)
                       
    return "Predicted Class is: {}".format(categories[np.argmax(prediction)])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=False)
