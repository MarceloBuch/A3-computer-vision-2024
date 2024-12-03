from app import create_app
from app.processor import process_video
import threading

# Cria o banco de dados (se ainda não existir)
app = create_app()

#ID do ônibus
id_bus = 1

# Inicia o processamento contínuo em um thread
thread = threading.Thread(target=process_video, args=(id_bus, app))
thread.daemon = True
thread.start()

# Inicia a aplicação Flask
if __name__ == "__main__":
    app.run(debug=True)