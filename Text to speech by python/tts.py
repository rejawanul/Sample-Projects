from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    
    # Text-to-speech conversion
    tts = gTTS(text=text, lang='en')
    
    # Save the MP3 file
    mp3_file_path = 'output.mp3'
    tts.save(mp3_file_path)
    
    return render_template('index.html', result='Conversion successful', audio_file=mp3_file_path)

@app.route('/download')
def download():
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)