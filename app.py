from flask import Flask, render_template
from config import DevelopmentConfig



APPLICATION_SETTINGS="./config.py"
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.static_url_path = app.config['STATIC_PTH']
app.static_folder = app.config['STATIC_FOLDER']



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])