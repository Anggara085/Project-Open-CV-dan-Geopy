import numpy as np
import cv2
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    file = request.files['image']
    # Proses gambar menggunakan OpenCV
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    # Tambahkan kode pengolahan gambar OpenCV di sini
    return jsonify(result="Image processed")

@app.route('/get-location', methods=['POST'])
def get_location():
    # Implementasi endpoint get-location
    pass

if __name__ == '__main__':
    app.run(debug=True)
