from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5000/add"

@app.route("/form")
def form():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    payload = {"name": name, "email": email, "message": message}

    try:
        response = requests.post(BACKEND_URL, json=payload)

        if response.ok:
            data = response.json()
            if data.get("status") == "success":
                return redirect(url_for("success"))
            else:
                flash(data.get("message", "Unknown error"))
                return redirect(url_for("form"))
        else:
            flash(f"Backend error: {response.status_code}")
            return redirect(url_for("submit"))

    except Exception as e:
        flash(str(e))
        return redirect(url_for("form"))

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(port=3000, debug=True)