from flask import Flask, render_template
import os

# serve assets/ under the /assets path so linked CSS/JS resolve
app = Flask(__name__, static_url_path="/assets", static_folder="assets")

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
