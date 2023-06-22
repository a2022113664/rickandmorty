import requests
import mysql.connector

# Função para obter os personagens de uma página específica e inseri-los no banco de dados
def obter_personagens_pagina(url, cursor):
    response = requests.get(url)
    data = response.json()
    personagens = data['results']

    for personagem in personagens:
        nome = personagem['name']
        cursor.execute("INSERT INTO personagens (nome) VALUES (%s)", (nome,))

    return data['info']['next']  # Retorna a URL da próxima página ou None se não houver mais páginas

# Configurações do banco de dados
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'almeidapewpew',
    'database': 'db_test'
}

# Cria uma conexão com o banco de dados
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Cria a tabela no banco de dados (se ainda não existir)
cursor.execute('''CREATE TABLE IF NOT EXISTS personagens
                  (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))''')

# URL inicial da API
url = 'https://rickandmortyapi.com/api/character'

# Percorre todas as páginas e obtém os personagens
while url:
    url = obter_personagens_pagina(url, cursor)
    conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
