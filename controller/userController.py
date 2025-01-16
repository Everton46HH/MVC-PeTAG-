from model.database import BancoDeDados
from dao.userDAO import userDAO

class userController:
    def __init__(self,user):
        self.user = user
        self.banco = BancoDeDados()
        self.conexao = self.banco.conectar()
        self.userDAO = userDAO(self.conexao)

    def mudarSenha(self,novaSenha):
        self.userDAO.atualizarSenha(self.user,novaSenha)
        self.user.setSenha(novaSenha)

    def mudarEmail(self,novoEmail):
        self.userDAO.atualizarSenha(self.user,novoEmail)
        self.user.setEmail(novoEmail)

    def adicionarUsuario(self, user):
        self.userDAO.addUser(user)
