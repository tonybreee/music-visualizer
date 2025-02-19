import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from visualization import generate_visualization

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
ALLOWED_EXTENSIONS = {"mp3", "wav"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return redirect(request.url)

    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        pixel_size = int(request.form["pixel_size"])
        animation_type = request.form["animation_type"]

        output_video_path = os.path.join(app.config["OUTPUT_FOLDER"], f"{filename}.mp4")
        generate_visualization(file_path, output_video_path, pixel_size, animation_type)

        return redirect(url_for("result", filename=f"{filename}.mp4"))

    return redirect(request.url)

@app.route("/result/<filename>")
def result(filename):
    return render_template("result.html", video_filename=filename)

@app.route("/download/<filename>")
def download_file(filename):
    return send_file(os.path.join(app.config["OUTPUT_FOLDER"], filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
