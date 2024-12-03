# Importando bibliotecas para o banco
from app import db
# Criando Classe 'Bus' para integrar ela mais facilmente
class Bus (db.Model):
    __tablename__ = 'buses'
    
    id = db.Column(db.Integer, primary_key=True)
    IDBus = db.Column(db.Integer, unique=True, nullable=False)
    Total = db.Column(db.Integer, default=0)
    Up = db.Column(db.Integer, default=0)
    Down = db.Column(db.Integer, default=0)

    def to_dict(self):
        return [{
            'IDBus': self.IDBus,
            'Total': self.Total,
            'Up': self.Up,
            'Down': self.Down
        }]
    
