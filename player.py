from flask import Flask, render_template, request
import os
import ffmpeg

app = Flask(__name__, template_folder='web')

@app.route('/')
def index():
    return render_template('player.html')

# Video-Decoding
    input_video = ffmpeg.input(output_path)
    output_video = ffmpeg.output(input_video, os.path.join('./uploads', f'decoded_{filename}'))
    ffmpeg.run(output_video)