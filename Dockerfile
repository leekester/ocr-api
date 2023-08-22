FROM ubuntu:22.04
RUN apt-get update
RUN apt install python3 python3-pip ffmpeg libgl1-mesa-glx curl -y
#RUN pip install paddlepaddle==2.4.0rc0 paddleocr==2.6.0.1 imutils==0.5.4 Pillow==9.5.0 opencv-python==4.5.5.64 numpy==1.23.5 Flask==2.3.2 matplotlib==3.6.0 easyocr==1.7.0
RUN pip install paddlepaddle==2.4.0rc0 paddleocr==2.6.0.1 Flask==2.3.2 easyocr==1.7.0
RUN mkdir -p /app/uploads
RUN chmod 777 /app/uploads
COPY initialize_models.py ocr_api.py sendimage.py hello.jpg /app/
RUN python3 /app/initialize_models.py
CMD ["python3", "/app/ocr_api.py"]
