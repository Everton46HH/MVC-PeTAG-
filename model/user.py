class User:
    def __init__(self, userId, nome, email, senha , telefone):
        self.userId = userId
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone

    def setSenha(self,novaSenha):
        self.senha = novaSenha

    def setEmail(self,novoEmail):
        self.email = novoEmail

    