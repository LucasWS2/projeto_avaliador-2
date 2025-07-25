import bcrypt
from models.usuario_model import UsuarioModel

class UsuarioController:
    @staticmethod
    def login(email, senha):
        usuario = UsuarioModel.buscar_por_email(email)
        if usuario and bcrypt.checkpw(senha.encode(), usuario["senha"].encode()):
            return usuario
        return None

    @staticmethod
    def cadastrar_usuario(nome, email, senha):
        existente = UsuarioModel.buscar_por_email(email)
        if existente:
            return False

        # Gera o hash da senha
        hashed = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        senha_hash = hashed.decode()  # salvar como string no banco

        sucesso = UsuarioModel.criar_usuario(nome, email, senha_hash)
        return sucesso
