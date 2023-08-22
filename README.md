# Background
This is an example of exposing an Optical Character Recognition (OCR) service as a RESTful API.
# Components
- Flask provides the web service
- EasyOCR and Paddle for OCR
# Image Size
The container image is REALLY large. The dependencies of EasyOCR are heavy, so removing that element would result in a significantly smaller image.
