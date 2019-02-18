# from api import create_app

# app = create_app('app')
from flask import Flask
from api import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)