from flask import Flask, render_template, request
import os
import ffmpeg

app = Flask(__name__, template_folder='web')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['video']
    filename = file.filename

    file_path = os.path.join('./uploads', filename)
    file.save(file_path)

    output_path = os.path.join('./uploads', f'encoded_{filename}')

    input_video = ffmpeg.input(file_path)
    output_video = input_video.h264()
    output_video = ffmpeg.output(output_video, output_path)
    ffmpeg.run(output_video)

    return 'Datei erfolgreich hochgeladen und encodiert.'


if __name__ == '__main__':
    app.run(debug=True)