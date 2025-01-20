from dao.databaseDAO import databaseDAO
from model.database import BancoDeDados

class databaseController:

     def __init__(self):
         self.banco = BancoDeDados()
         self.conexao = self.banco.conectar()
         self.dao = databaseDAO(self.conexao)

     def verDispositivosConectados(self):
          return self.dao.aparelhosConectados()
    
     def verificacao(self,userId,userSenha):
          return self.dao.verificacao(userId,userSenha)
     
     def localizacao(self,id):
          return self.dao.localizacao(id)
     
     def atualizarConexao(self):
          # Isso é necessario pois ele cria uma nova conexao ao banco de dados,permitindo a constante consulta das coordenadas
          self.banco = BancoDeDados()
          self.conexao = self.banco.conectar()
          self.dao = databaseDAO(self.conexao)
         