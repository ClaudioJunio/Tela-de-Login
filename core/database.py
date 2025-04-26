# Importa a biblioteca json para manipular arquivos JSON
import json
import os

# Define o caminho do arquivo JSON que simula o banco de dados
DATA_PATH = os.path.join("data", "users.json")

# Função para carregar os usuários do arquivo JSON
def load_users():
    # Verifica se o arquivo existe
    if not os.path.exists(DATA_PATH):
        return []  # Retorna lista vazia se o banco ainda não existe

    # Abre e lê o conteúdo do arquivo JSON
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  # Retorna lista vazia em caso de erro no arquivo

# Função para buscar um usuário pelo nome de usuário
def get_user_by_username(username):
    # Carrega a lista de usuários
    users = load_users()

    # Procura um usuário cujo campo "username" seja igual ao que foi passado
    for user in users:
        if user.get("username") == username:
            return user  # Retorna o usuário encontrado

    return None  # Se não encontrar, retorna None