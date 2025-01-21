class userDAO:

    def __init__(self,conexao):
        self.conexao = conexao

    def atualizarSenha(self,user,novaSenha):
        cursor = self.conexao.cursor()
        cursor.execute(f"UPDATE Usuario set senha = '{novaSenha}' where userID = {user.userId}")
        self.conexao.commit()

    def atualizarEmail(self,user,novoEmail):

        cursor = self.conexao.cursor()
        
        cursor.execute(f"UPDATE Usuario set email={novoEmail} where userID = {user.userId}")
        self.conexao.commit()

    def addUser(self, user):
        cursor = self.conexao.cursor()
        try:
            query = """
            INSERT INTO Usuario (nome, email, senha, telefone) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (user.nome, user.email, user.senha, user.telefone))
            self.conexao.commit()
            
            userId = cursor.lastrowid
            
            print(f"Usuário adicionado com sucesso! O ID gerado é: {userId},NÃO SE ESQUEÇA DELE")

        except Exception as e:
            print(f"FALHA AO ADICIONAR O USUARIO,{e}")
            return False

        finally:
            cursor.close()
