from database.conexao import conectar

class ClienteModel:
    @staticmethod
    def criar(nome, telefone, email):
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, telefone, email))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return clientes
