from database.conexao import conectar

class VendaModel:
    @staticmethod
    def registrar_venda(cliente_id, itens, total):
        conn = conectar()
        cursor = conn.cursor()

        # Registrar venda
        sql_venda = "INSERT INTO vendas (cliente_id, total) VALUES (%s, %s)"
        cursor.execute(sql_venda, (cliente_id, total))
        venda_id = cursor.lastrowid

        # Registrar itens da venda
        sql_item = "INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)"
        for item in itens:
            cursor.execute(sql_item, (
                venda_id,
                item["produto_id"],
                item["quantidade"],
                item["preco_unitario"]
            ))

        conn.commit()
        cursor.close()
        conn.close()
