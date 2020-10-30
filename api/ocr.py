import io
import requests
import pytesseract
from PIL import Image
from flask import Flask, request, jsonify

app = Flask(__name__)
app.debug = False

@app.route('/')
def xyz():
    message = "Hello, World!"
    return message

@app.route('/ocr')
def ocr():
    url = request.args['url']
    try:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        text = pytesseract.image_to_string(image)
        status = 'true'
    except OSError:
        status = 'false'
        text = "INVALID_URL"
    if not text:
        text = "TEXT_NOT_FOUND"
    result = jsonify(
        ok=status,
        text=text
    )
    return result

if __name__ == '__main__':
    app.run()
