class databaseDAO:
    def __init__(self,conexao):
        self.conexao = conexao

    def aparelhosConectados(self):

        cursor = self.conexao.cursor()
        cursor.execute("SELECT idDispositivo,nomeDispositivo FROM Dispositivo")

        dispositivos = cursor.fetchall()

        return dispositivos
    
    def verificacao(self,userId,userSenha):

        cursor = self.conexao.cursor()
        cursor.execute(f"SELECT * FROM Usuario WHERE userID = {userId}")
        data = cursor.fetchone()
        cursor.close()

        try:
            senha = data[3]
            if userSenha == senha:
                return data
            
        except:
            return None
        
        else:
            return ''
        
    def localizacao(self,id):
        
        cursor = self.conexao.cursor()
        cursor.execute(f"SELECT idDispositivo, nomeDispositivo, latitude, longitude FROM Dispositivo WHERE idDispositivo = {id}")
        loc = cursor.fetchone()
        cursor.close()

        try:
            if loc:
                return loc
            
        except:
            return None
        
    def adicionarRegistro(self,id,registro):
        cursor = self.conexao.cursor()
        cursor.execute(f"INSERT INTO HistoricoCoordenadas(idDispositivo,latitude,longitude) VALUES({registro[0]}, {registro[2]}, {registro[3]})")
        cursor.close()
        self.conexao.commit()
