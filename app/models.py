#Criando Classe 'Bus' para integrar ela mais facilmente
class Bus ():
    
    # Definindo parametros
    def __init__(self, IDBus):
        self.IDBus = IDBus
        self.Total = 0
        self.Up = 0
        self.Down = 0

    # Função para achar o centro do objeto, será utilizada na detecção dele
    def center(self, x, y, w, h):
        x1 = int(w / 2)
        y1 = int(h / 2)

        cx = x + x1
        cy = y + y1

        return cx, cy
    
if __name__ == '__main__':
    Bus.init_db()