from app import db
from app.models import Bus
from app.detection import detectionVideo

def process_video(id_bus, app):

    for result in detectionVideo():
        # Extrai os dados
        up = result['up']
        down = result['down']
        total = result['total']

        # Verifica se o registro já existe no banco
        with app.app_context():
            bus = Bus.query.filter_by(IDBus=id_bus).first()
            if not bus:
                # Cria um novo registro se ele não existir
                bus = Bus(IDBus=id_bus, Up=up, Down=down, Total=total)
                db.session.add(bus)
            else:
                # Atualiza os valores
                bus.Up = up
                bus.Down = down
                bus.Total = total

            db.session.commit()

            db.session.refresh(bus)


        print(f"Atualizado: IDBus={bus.IDBus}, UP={bus.Up}, DOWN={bus.Down}, TOTAL={bus.Total}")