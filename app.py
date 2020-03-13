from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

DL_DIR = "downloads"
AUDIO_DIR = DL_DIR + "/audio"
VIDEO_DIR = DL_DIR + "/video"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/dl", methods=["GET"])
def download():
    # Fetch the form data
    url = request.args.get("url", None)
    dlformat = request.args.get("format", None)
    
    if url:
        if dlformat == "audio":
            status_code = subprocess.call(["youtube-dl", "-x", url])
            if status_code == 0:
                return 'OK'
        elif dlformat == "video":
            status_code = subprocess.call(["youtube-dl", url])
            if status_code == 0:
                return 'OK'
    return 'NOT OK'
