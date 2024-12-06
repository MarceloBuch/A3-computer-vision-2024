from flask import jsonify, render_template
from app.models import Bus
from app import create_app
from app.processor import process_video
import threading

# Cria o banco de dados (se ainda não existir)
app = create_app()

#ID do ônibus
id_bus = 1

# Definindo rotas da API
@app.route("/index")
def index():
    buses = Bus.query.all()
    return render_template("./index.html", buses=buses)

@app.route("/list", methods=["GET"])
def list_bus_data():
    buses = Bus.query.all()
    return jsonify([bus.to_dict() for bus in buses])

# Inicia o processamento contínuo em um thread
thread = threading.Thread(target=process_video, args=(id_bus, app))
thread.daemon = True
thread.start()

# Inicia a aplicação Flask
if __name__ == "__main__":
    app.run(debug=False)