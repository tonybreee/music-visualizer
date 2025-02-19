from flask import Flask, render_template, request, redirect, session
from app.spotify_api import spotify_login, get_spotify_song
from app.visualization import create_animation

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/spotify")
def login_spotify():
    return redirect(spotify_login())

@app.route("/callback/spotify")
def callback_spotify():
    session["spotify_token"] = request.args.get("code")
    return redirect("/")

@app.route("/generate", methods=["POST"])
def generate():
    song_id = request.form["song_id"]
    song_data = get_spotify_song(song_id, session["spotify_token"])

    video_path = create_animation(song_data["album_cover"], 5, "Kreis", song_data["bpm"], 10)
    return render_template("result.html", video_file=video_path)
