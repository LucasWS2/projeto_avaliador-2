from database.conexao import conectar

class ProdutoModel:
    @staticmethod
    def criar(nome, preco, estoque):
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, preco, estoque))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        conn.close()
        return produtos
