from paddleocr import PaddleOCR,draw_ocr
import easyocr
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True, debug=False, show_log = False, ocr_version='PP-OCR')
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True, debug=False, show_log = False, ocr_version='PP-OCRv2')
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True, debug=False, show_log = False, ocr_version='PP-OCRv3')
ocr = easyocr.Reader(['en'])
