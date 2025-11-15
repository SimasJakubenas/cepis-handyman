from flask import Blueprint, render_template, jsonify
import json, os
from app.supabase_client import supabase

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

@main.route("/admin")
def admin():
    return render_template("admin.html")

@main.route("/dbcheck")
def dbcheck():
    try:
        response = supabase.table('project').select('*').limit(1).execute()
        if response.data is not None:
            return f"Connected to Supabase! {response.data}"
        else:
            return f"Connection failed: {response}"
    except Exception as e:
        return f"Error connecting to Supabase: {e}"