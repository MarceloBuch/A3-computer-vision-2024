from flask import jsonify, render_template
from app import app, db
from app.models import Bus

@app.route("/")
def index():
    buses = Bus.query.all()
    return render_template("templates/index.html", buses=buses)

@app.route("/list", methods=["GET"])
def list_bus_data():
    buses = Bus.query.all()
    return jsonify([bus.to_dict() for bus in buses])

@app.route("/reset/<int:id_bus>", methods=["POST"])
def reset_bus_data(id_bus):
    bus = Bus.query.filter_by(IDBus=id_bus).first()
    if bus:
        bus.up = 0
        bus.down = 0
        bus.total = 0
        db.session.commit()
        return (
            jsonify({"message": f"Dados do ônibus {id_bus} reiniciados com sucesso."}),
            200,
        )
    return jsonify({"error": "Ônibus não encontrado."}), 404

@app.route("/bus/<int:id_bus>", methods=["GET"])
def get_bus(id_bus):
    bus = Bus.query.filter_by(IDBus=id_bus).first()
    if bus:
        return jsonify(bus.to_dict())
    return jsonify({"error": "Bus not found"}), 404
