from flask import Flask, render_template, request, redirect
import speech_recognition as sr

"""
Tutorial is here. Posted July 31, 2020. Accessed October 25, 2020.
https://www.youtube.com/watch?v=vuaolF-OSGY
"""

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ''
    if request.method == 'POST':
        print('form data recieved')

        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file:
            # Thing that understands and transcribes
            recognizer = sr.Recognizer()
            audio_file = sr.AudioFile(file)
            with audio_file as source:
                # Original output for the given file
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            print(transcript)

        return render_template('index.html', transcript=transcript)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
