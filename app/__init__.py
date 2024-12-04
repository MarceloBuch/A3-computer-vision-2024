from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa a instância do SQLAlchemy sem associar ao app diretamente
db = SQLAlchemy()


def create_app():
    # Cria a instância do aplicativo Flask
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bus_data.db"

    # Inicializa o banco de dados com o app
    db.init_app(app)

    with app.app_context():
        try:
            db.create_all()
        except Exception as exception:
            print(
                "got the following exception when attempting db.create_all() in __init__.py: "
                + str(exception)
            )
        finally:
            print(
                "db.create_all() in __init__.py was successfull - no exceptions were raised"
            )

    return app
