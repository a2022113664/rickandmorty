import requests
import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='172.17.0.2',
    user='root',
    password='almeidapewpew',
    database='db_test'
)
c = conn.cursor()

# Criar tabela de personagens
c.execute('''CREATE TABLE IF NOT EXISTS personagens
              (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))''')

# Obter personagens
url = 'https://rickandmortyapi.com/api/character'
while url:
    response = requests.get(url)
    data = response.json()
    personagens = data['results']

    # Inserir nomes dos personagens na tabela
    for personagem in personagens:
        nome = personagem['name']
        c.execute("INSERT INTO personagens (nome) VALUES (%s)", (nome,))

    url = data['info']['next']

# Criar tabela de locations
c.execute('''CREATE TABLE IF NOT EXISTS locations
              (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))''')

# Obter locations
url = 'https://rickandmortyapi.com/api/location'
while url:
    response = requests.get(url)
    data = response.json()
    locations = data['results']

    # Inserir nomes das locations na tabela
    for location in locations:
        nome = location['name']
        c.execute("INSERT INTO locations (nome) VALUES (%s)", (nome,))

    url = data['info']['next']

# Salvar alterações e fechar conexão
conn.commit()
conn.close()
