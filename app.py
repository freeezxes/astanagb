from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# --- новые маршруты ---
@app.route("/offer")
def offer():
    return render_template("offer.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
# ----------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
