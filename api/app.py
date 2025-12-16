from flask import Flask
from bson.json_util import dumps
from users import usersBlueprint
from mongo import provinces
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.register_blueprint(usersBlueprint)



@app.route("/")
def main_page():
    return "Nagarpalika app"

@app.route("/province-data")
def getProvinceData():
    return dumps(provinces.find())

if __name__ == "__main__":
    app.run(debug=True)