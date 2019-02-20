from flask import Flask
from api.swagger import blueprint


app = Flask(__name__)
app.register_blueprint(blueprint)
# app.config.SWAGGER_UI_TRY_IT_OUT

if __name__ == '__main__':
    app.run(debug=True)
