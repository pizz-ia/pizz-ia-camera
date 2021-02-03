export FLASK_APP=src/app.py
modprobe bcm2835-v4l2 && python -m flask run --host=0.0.0.0