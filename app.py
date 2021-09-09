from flask import Flask, render_template
from config import DevelopmentConfig



APPLICATION_SETTINGS="./config.py"
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.static_url_path = app.config.get('STATIC_PTH')
app.static_folder = app.config.get('STATIC_FOLDER')
# app.config['ASSETS_PTH'] = {'dev':"static", 'prod':"static"}



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()