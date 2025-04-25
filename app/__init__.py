# app/__init__.py
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from functools import wraps

app = Flask(__name__)
app.secret_key = '12345678'

clients = []
programs = []
client_id_counter = 1

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin123":
            session["logged_in"] = True
            return redirect(url_for("index"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

@app.route("/", methods=["GET"])
@login_required
def index():
    search_query = request.args.get("search", "").lower()
    filtered_clients = [c for c in clients if search_query in c["name"].lower()] if search_query else clients
    return render_template("index.html", clients=filtered_clients, programs=programs)

@app.route("/register_client", methods=["POST"])
@login_required
def register_client():
    global client_id_counter
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    client = {
        "id": client_id_counter,
        "name": name,
        "age": age,
        "gender": gender,
        "programs": []
    }
    clients.append(client)
    client_id_counter += 1
    return redirect(url_for("index"))

@app.route("/create_program", methods=["POST"])
@login_required
def create_program():
    program_name = request.form["program_name"]
    description = request.form["description"]
    programs.append({"name": program_name, "description": description})
    return redirect(url_for("index"))

@app.route("/enroll", methods=["POST"])
@login_required
def enroll():
    client_id = int(request.form["client_id"])
    selected_programs = request.form.getlist("programs")
    for client in clients:
        if client["id"] == client_id:
            for p in selected_programs:
                if p not in client["programs"]:
                    client["programs"].append(p)
    return redirect(url_for("index"))

@app.route("/client/<int:client_id>")
@login_required
def view_profile(client_id):
    client = next((c for c in clients if c["id"] == client_id), None)
    if client:
        return render_template("profile.html", client=client)
    return "Client not found", 404

@app.route("/api/client/<int:client_id>")
@login_required
def get_client_api(client_id):
    client = next((c for c in clients if c["id"] == client_id), None)
    if client:
        return jsonify(client)
    return jsonify({"error": "Client not found"}), 404
