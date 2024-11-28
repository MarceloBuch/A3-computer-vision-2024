# Importando bibliotecas para o banco
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base

# Criando o banco de dados para armezenar os resultados 
engine = create_engine('sqlite:///dbBus.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

# Criando Classe 'Bus' para integrar ela mais facilmente
class Bus (Base):
    # Definindo tabela no banco
    __tablename__ = 'Bus'

    IDBus = Column(Integer, primary_key=True)
    Total = Column(Integer, default=0)
    Up = Column(Integer, default=0)
    Down = Column(Integer, default=0)
    
    # Definindo parametros
    def __init__(self, IDBus):
        self.IDBus = IDBus
        self.Total = 0
        self.Up = 0
        self.Down = 0

    def __repr__(self):
        return [{
            'IDBus': self.IDBus,
            'Total': self.Total,
            'Up': self.Up,
            'Down': self.Down
        }]

    def init_db():
        Base.metadata.create_all(bind=engine)

    def incrementUp(self):
        self.Up += 1
    
    def incrementDown(self):
        self.Down += 1
        
    def incrementTotal(self):
        self.Total += 1

    # Função para achar o centro do objeto, será utilizada na detecção dele
    def center(self, x, y, w, h):
        x1 = int(w / 2)
        y1 = int(h / 2)

        cx = x + x1
        cy = y + y1

        return cx, cy
    
if __name__ == '__main__':
    Bus.init_db()