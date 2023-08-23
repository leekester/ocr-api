# Background
This is an example of exposing an Optical Character Recognition (OCR) service as a RESTful API.\
As multiple OCR engines and models are running, the consumer can choose which engine/model to carry out the recognition - or execute against all models and parse the output.\
This isn't production-ready, but hopefully is a useful starter for anyone looking to build a similar capability.
# Components
- I've run this on Ubuntu 22.04. Works both on an IaaS VM or in a container
- Flask provides the web service
- EasyOCR and Paddle for OCR
# Image Size
The container image is **REALLY** large. The dependencies of EasyOCR are heavy, so removing that element would result in a significantly smaller image.\
I tried using a more lightweight base image (Alpine) although wasn't able to get PaddlePaddle to function with it.
# Usage
## Container
Build using the Dockerfile. Listens on the default Flask port of 5000.
As mentioned, the image is pretty large, and will take a while to push and pull.
## Ubuntu Server
Clone this repo, change directory into the base directory and:
```
matt@ocr:~$ apt-get update
matt@ocr:~$ apt install python3 python3-pip libgl1-mesa-glx curl -y
matt@ocr:~$ pip install paddlepaddle==2.4.0rc0 paddleocr==2.6.0.1 imutils==0.5.4 Pillow==9.5.0 opencv-python==4.5.5.64 numpy==1.23.5 Flask==2.3.2 matplotlib==3.6.0 easyocr==1.7.0
matt@ocr:~$ mkdir -p /app/uploads
matt@ocr:~$ chmod 777 /app/uploads
matt@ocr:~$ cp * /app/
matt@ocr:~$ python3 /app/ocr_api.py
```
## Calling the Service
An example call to the service is included in the repo as sendimage.py.\
The service returns a JSON response such as the one below. To only run the image through a single model, specify it in the 'model' HTTP header. Details are in sendimage.py.
In my testing, PPOCR-v3 has been the winner in terms of accuracy.
```
[
	[{
		"text": "HELLO WORLD",
		"confidence": 0.9998155695810481,
		"model": "easyocr",
		"processing_time_ms": 304.94,
		"correlation_id": "274a024c-1571-49db-af82-2df5d23df3bd"
	}],
	[{
		"text": "HELLOWORLD",
		"confidence": 0.9997454881668091,
		"model": "ppocr",
		"processing_time_ms": 75.31,
		"correlation_id": "9a00de4a-0b22-4c25-924b-35b4115f53ff"
	}],
	[{
		"text": "HELLOWORLD",
		"confidence": 0.9898713231086731,
		"model": "ppocrv2",
		"processing_time_ms": 85.71,
		"correlation_id": "bea9806d-da5d-4a8e-b506-2857173236e7"
	}],
	[{
		"text": "HELLO WORLD",
		"confidence": 0.9897682666778564,
		"model": "ppocrv3",
		"processing_time_ms": 137.64,
		"correlation_id": "97db6f59-20e9-40d4-bfc8-f221590e7612"
	}]
]
```
