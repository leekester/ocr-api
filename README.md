# Background
This is an example of exposing an Optical Character Recognition (OCR) service as a RESTful API.
# Components
- I've run this on Ubuntu 22.04. Works both on an IaaS VM or in a container
- Flask provides the web service
- EasyOCR and Paddle for OCR
# Image Size
The container image is REALLY large. The dependencies of EasyOCR are heavy, so removing that element would result in a significantly smaller image.
I tried using a more lightweight base image (Alpine) although wasn't able to get PaddlePaddle to function with it.
# Usage
## Container
Build using the Dockerfile. Listens on the default Flask port of 5000
As mentioned, the image is pretty large, and will take a while to pull.
## Ubuntu Server
Clone this repo, change directory into the base directory and:
```
# apt-get update
# apt install python3 python3-pip libgl1-mesa-glx curl -y
# pip install paddlepaddle==2.4.0rc0 paddleocr==2.6.0.1 imutils==0.5.4 Pillow==9.5.0 opencv-python==4.5.5.64 numpy==1.23.5 Flask==2.3.2 matplotlib==3.6.0 easyocr==1.7.0
# mkdir -p /app/uploads
# chmod 777 /app/uploads
# cp * /app/
# python3 /app/ocr_api.py
```
