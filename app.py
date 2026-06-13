from flask import Flask

app = Flask(__name__)

@app.route("/resume")
def resume():
    return "<h1>Future SOC Analyst</h1>"

@app.route("/about")
def about():
    return "<h1>About Nick</h1>"

app.run(host="0.0.0.0", port=5000)