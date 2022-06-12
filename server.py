import imghdr
import os
from flask import Flask, redirect, url_for, render_template, request, abort, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.wav', '.mp3', '.m4a']
app.config['UPLOAD_PATH'] = os.getcwd() + '/uploads'

def split(filename):
    os.system("spleeter separate -o audio_output -p spleeter:4stems " + str(os.path.join(app.config['UPLOAD_PATH'], filename)))

@app.route('/')
def index():
   files = os.listdir(app.config['UPLOAD_PATH'])
   return render_template('index.html')
	
@app.route('/', methods = ['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return "Invalid file type", 400
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        split(filename)
    return '', 204

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == '__main__':
    # Replace the 127.0.0.1 below with the appropriate host, if not hosted locally
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=False)