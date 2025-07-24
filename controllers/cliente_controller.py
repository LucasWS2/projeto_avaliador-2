from models.cliente_model import ClienteModel

class ClienteController:
    @staticmethod
    def cadastrar(nome, telefone, email):
        ClienteModel.criar(nome, telefone, email)

    @staticmethod
    def listar_clientes():
        return ClienteModel.listar()
