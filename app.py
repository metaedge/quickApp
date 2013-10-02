import os
from flask import Flask, render_template, send_from_directory
# -------------------------
#      init
# -------------------------
app = Flask(__name__)

app.config.update(
    DEBUG = True,
)

app.config["SECRET_KEY"] = 'a\xf1\xe3\xc3\x13[^\xa9\x87\xdd\xafv\x14\xc5\xd9r\x1e\x05&\x9cP\xe7\xf3\xa2'

#----------------------------------------
# database
#----------------------------------------

from mongoengine import connect
from flask.ext.mongoengine import MongoEngine

DB_NAME = 'metaedge'
DB_USERNAME = 'metaedge'
DB_PASSWORD = 'spring'
DB_HOST_ADDRESS = 'ds047448.mongolab.com:47448/metaedge'

app.config["MONGODB_DB"] = DB_NAME
connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)
db = MongoEngine(app)

# -------------------------
#    controllers
# -------------------------
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.route_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html') 

# -------------------------
# 	launch
# -------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
