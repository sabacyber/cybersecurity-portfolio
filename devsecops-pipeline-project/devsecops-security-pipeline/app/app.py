from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Security Pipeline Demo"

@app.route("/ping")
def ping():
    host = request.args.get("host")
    os.system(f"ping -c 1 {host}")
    return "Ping executed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
