from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "devsecops123":
            return redirect(url_for("dashboard"))

        return "Invalid username or password."

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/status")
def api_status():
    return jsonify(
        {
            "application": "Secure DevSecOps Demo",
            "status": "running",
            "environment": "development"
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


app.run(host="0.0.0.0", port=5050, debug=True)
