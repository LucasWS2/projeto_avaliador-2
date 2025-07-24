from models.produto_model import ProdutoModel

class ProdutoController:
    @staticmethod
    def cadastrar(nome, preco, estoque):
        ProdutoModel.criar(nome, preco, estoque)

    @staticmethod
    def listar_produtos():
        return ProdutoModel.listar()
