from flask import Flask
from bson.json_util import dumps
from users import usersBlueprint
from mongo import provinces, mongo_url
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.register_blueprint(usersBlueprint)



@app.route("/")
def main_page():
    return "Nagarpalika app"

@app.route("/province-data")
def getProvinceData():
    print(mongo_url)
    return dumps(provinces.find())

if __name__ == "__main__":
    app.run(debug=True)