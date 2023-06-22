import requests
import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='almeidapewpew',
    database='db_test'
)
c = conn.cursor()

# Obter personagens
url = 'https://rickandmortyapi.com/api/character'
response = requests.get(url)
data = response.json()
personagens = data['results']

# Criar tabela de personagens
c.execute('''CREATE TABLE IF NOT EXISTS personagens
              (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))''')

# Inserir nomes dos personagens na tabela
for personagem in personagens:
    nome = personagem['name']
    c.execute("INSERT INTO personagens (nome) VALUES (%s)", (nome,))

# Obter locais
url_locations = 'https://rickandmortyapi.com/api/location'
response_locations = requests.get(url_locations)
data_locations = response_locations.json()
locations = data_locations['results']

# Criar tabela de locais
c.execute('''CREATE TABLE IF NOT EXISTS locations
              (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))''')

# Inserir nomes dos locais na tabela
for location in locations:
    nome = location['name']
    c.execute("INSERT INTO locations (nome) VALUES (%s)", (nome,))

# Salvar alterações e fechar conexão
conn.commit()
conn.close()
