import os
import time
from api.API import APIClient
from camera.Camera import Camera
from flask import Flask

app = Flask(__name__)

SAVE_PICTURE_PATH = "/data"
cam = Camera()

@app.route('/picture')
def take_picture():
    picture_path = cam.shoot(SAVE_PICTURE_PATH, "python-test")
    print("Picture taked")

    api = APIClient("https://api.pizzia.k8s.jeremychauvin.fr")
    api.predict(picture_path)