from database.conexao import conectar

class UsuarioModel:
    @staticmethod
    def criar_usuario(nome, email, senha):
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, senha))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_por_email(email):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(sql, (email,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado

    @staticmethod
    def listar_usuarios():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios
