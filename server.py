#ejecutar nuestra aplicación
#1 pipenv install flask pymysql flask-bcrypt
#2 pipenv shell
#3 py server.py
from flask_app import app


#importando mi controlador
from flask_app.controllers import users_controller, recipes_controller


if __name__ == '__main__':
    app.run(debug=True)