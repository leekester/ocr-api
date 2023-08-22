import os
import json
import datetime
import uuid
from flask import Flask, request, jsonify
from paddleocr import PaddleOCR,draw_ocr
import easyocr

ocr_easyocr = easyocr.Reader(['en'])
ocr_ppocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True, debug=False, show_log=False, ocr_version='PP-OCR')
ocr_ppocrv2 = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True, debug=False, show_log=False, ocr_version='PP-OCRv2')
ocr_ppocrv3 = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True, debug=False, show_log=False, ocr_version='PP-OCRv3')
global run_all_models

app = Flask(__name__)

# Set the maximum allowed file size (in bytes)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

# Specify the directory where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def fn_easyocr(img_path):
    results = []
    start = datetime.datetime.now()
    ocr_results = ocr_easyocr.readtext(img_path)
    ocr_version = 'easyocr'
    if not ocr_results:
        ocr_results = [[[[5.0, 7.0], [85.0, 5.0], [85.0, 25.0], [5.0, 27.0]], ('', 0)]]
    correlation_id = uuid.uuid4()
    for ocr_result in ocr_results:
        if ocr_result:
            text = ocr_result[1]
            confidence = ocr_result[2]
            end = datetime.datetime.now()
            processing_time_ms = round(((end - start).total_seconds() * 1000), 2)
            temp_object = {
                "text": text,
                "confidence": confidence,
                "model": ocr_version,
                "processing_time_ms": processing_time_ms,
                "correlation_id": str(correlation_id)
            }
        else:
            end = datetime.datetime.now()
            processing_time_ms = round(((end - start).total_seconds() * 1000), 2)
            temp_object = {
                "text": "",
                "confidence": 0,
                "model": ocr_version,
                "processing_time_ms": processing_time_ms,
                "correlation_id": str(correlation_id)
            }
        results.append(temp_object)
    return results

def fn_ppocr(img_path):
    results = []
    start = datetime.datetime.now()
    ocr_results = ocr_ppocr.ocr(img_path, cls=True)
    print("Printing ocr_results...")
    print(ocr_results)
    ocr_version = 'ppocr'
    if not ocr_results:
        ocr_results = [[[[5.0, 7.0], [85.0, 5.0], [85.0, 25.0], [5.0, 27.0]], ('', 0)]]
    correlation_id = uuid.uuid4()
    for ocr_result in ocr_results:
        if ocr_result:
            print("Printing ocr_result...")
            print(ocr_result)
            print("Printing ocr_result[0]...")
            print(ocr_result[0][0])
            text = ocr_result[1][0]
            print("Printing text...")
            print(text)
            print("Printing confidence..")
            confidence = ocr_result[1][1]
            print(confidence)
            end = datetime.datetime.now()
            processing_time_ms = round(((end - start).total_seconds() * 1000), 2)
            temp_object = {
                "text": text,
                "confidence": confidence,
                "model": ocr_version,
                "processing_time_ms": processing_time_ms,
                "correlation_id": str(correlation_id)
            }
        else:
            end = datetime.datetime.now()
            processing_time_ms = round(((end - start).total_seconds() * 1000), 2)
            temp_object = {
                "text": "",
                "confidence": 0,
                "model": ocr_version,
                "processing_time_ms": processing_time_ms,
                "correlation_id": str(correlation_id)
            }
        results.append(temp_object)
    return results


def fn_ppocrv2(img_path):
    results = []
    start = datetime.datetime.now()
    ocr_results = ocr_ppocrv2.ocr(img_path, cls=True)
    ocr_version = 'ppocrv2'
    if not ocr_results:
        ocr_results = [[[[5.0, 7.0], [85.0, 5.0], [85.0, 25.0], [5.0, 27.0]], ('', 0)]]
    correlation_id = uuid.uuid4()
    for ocr_result in ocr_results:
        if ocr_result:
            text = ocr_result[1][0]
            confidence = ocr_result[1][1]
            end = datetime.datetime.now()
            processing_time_ms = round(((end - start).total_seconds() * 1000), 2)
            temp_object = {
                "text": text,
                "confidence": confidence,
                "model": ocr_version,
                "processing_time_ms": processing_time_ms,
                "correlation_id": str(correlation_id)
            }
        else:
            end = datetime.datetime.now()
            processing_time_ms = round(((end - start).total_seconds() * 1000), 2)
            temp_object = {
                "text": "",
                "confidence": 0,
                "model": ocr_version,
                "processing_time_ms": processing_time_ms,
                "correlation_id": str(correlation_id)
            }
        results.append(temp_object)
    return results

def fn_ppocrv3(img_path):
    results = []
    start = datetime.datetime.now()
    ocr_results = ocr_ppocrv3.ocr(img_path, cls=True)
    ocr_version = 'ppocrv3'
    if not ocr_results:
        ocr_results = [[[[5.0, 7.0], [85.0, 5.0], [85.0, 25.0], [5.0, 27.0]], ('', 0)]]
    correlation_id = uuid.uuid4()
    for ocr_result in ocr_results:
        if ocr_result:
            text = ocr_result[1][0]
            confidence = ocr_result[1][1]
            end = datetime.datetime.now()
            processing_time_ms = round(((end - start).total_seconds() * 1000), 2)
            temp_object = {
                "text": text,
                "confidence": confidence,
                "model": ocr_version,
                "processing_time_ms": processing_time_ms,
                "correlation_id": str(correlation_id)
            }
        else:
            end = datetime.datetime.now()
            processing_time_ms = round(((end - start).total_seconds() * 1000), 2)
            temp_object = {
                "text": "",
                "confidence": 0,
                "model": ocr_version,
                "processing_time_ms": processing_time_ms,
                "correlation_id": str(correlation_id)
            }
        results.append(temp_object)
    return results

@app.route('/ocr', methods=['POST'])

def upload_file():
    start = datetime.datetime.now()
    model = str(request.headers.get("model"))

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate file extension (optional)
    allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    if not allowed_file(file.filename, allowed_extensions):
        return jsonify({'error': 'Invalid file extension'}), 400

    # Save the file to the specified directory
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    img_path = (os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    global ocr
    if model == 'easyocr':
        output = fn_easyocr(img_path)
    elif model == 'ppocr':
        output = fn_ppocr(img_path)
    elif model == 'ppocrv2':
        output = fn_ppocrv2(img_path)
    elif model == 'ppocrv3':
        output = fn_ppocrv3(img_path)
    elif model == 'all':
        output_array = []
        output_array.append(fn_easyocr(img_path))
        output_array.append(fn_ppocr(img_path))
        output_array.append(fn_ppocrv2(img_path))
        output_array.append(fn_ppocrv3(img_path))
        output = output_array
    else:
        errorstate = True
        output = fn_ppocrv3(img_path)
        print('Didn\'t match a model. Using default of PPOCRv3')

    result = json.dumps(output)
    return result

def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
