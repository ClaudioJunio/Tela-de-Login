# Importa a biblioteca hashlib para gerar hashes seguros
import hashlib

# Importa a função que busca usuários cadastrados no banco
from core.database import get_user_by_username

# Função que gera o hash SHA-256 da senha digitada
def hash_password(password):
    # Codifica a string e gera o hash
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Função que verifica as credenciais de login
def authenticate(username, password):
    # Busca o usuário no banco de dados (JSON)
    user = get_user_by_username(username)

    # Se o usuário não existir, retorna False
    if user is None:
        return False

    # Gera o hash da senha digitada
    hashed_input = hash_password(password)

    # Compara o hash da senha digitada com o hash salvo no banco
    return hashed_input == user["password"]