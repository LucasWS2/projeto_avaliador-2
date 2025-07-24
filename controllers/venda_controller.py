from models.venda_model import VendaModel

class VendaController:
    @staticmethod
    def registrar(cliente_id, itens, total):
        VendaModel.registrar_venda(cliente_id, itens, total)
