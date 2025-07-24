from models.usuario_model import UsuarioModel

class UsuarioController:
    @staticmethod
    def login(email, senha):
        usuario = UsuarioModel.buscar_por_email(email)
        if usuario and usuario["senha"] == senha:
            return usuario  # Retorna o dicionário com nome, email etc.
        return None
