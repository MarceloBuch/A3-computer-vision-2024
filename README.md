
# Contador de Pessoas no Ônibus com Flask e API

Este projeto é uma aplicação desenvolvida em Python que utiliza OpenCV para visão computacional e Flask para criar uma API em tempo real dos dados. O sistema processa vídeos, identificando o número de pessoas subindo e descendo de um ônibus, além de calcular o total de pessoas presentes. Os dados são armazenados em um banco de dados SQLite e podem ser acessados por meio de uma interface web.

---

## 💻 **Como Executar o Projeto**

Siga os passos abaixo para configurar e rodar o projeto localmente:

### 1. Clone o repositório
```bash
git clone https://github.com/MarceloBuch/A3-computer-vision-2024.git
```

### 2. Crie o ambiente virtual
```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual
```bash
./.venv/scripts/activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Rode o programa
```bash
python run.py
```

### 6. Teste a API
Abra o navegador ou ferramentas como Postman e acesse o endereço:
[http://127.0.0.1:5000/index](http://127.0.0.1:5000/index)

