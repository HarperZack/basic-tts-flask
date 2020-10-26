from flask import Flask, render_template
import speech_recognition as sr

"""
Tutorial is here. Posted July 31, 2020. Accessed October 25, 2020.
https://www.youtube.com/watch?v=vuaolF-OSGY
"""

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
