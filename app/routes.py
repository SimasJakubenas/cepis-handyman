from flask import Blueprint, render_template, jsonify
import json, os

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/gallery")
def gallery():
    path = os.path.join(os.path.dirname(__file__), "gallery.json")
    with open(path) as f:
        images = json.load(f)
    return render_template("gallery.html", images=images)