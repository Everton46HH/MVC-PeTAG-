import mysql.connector

class BancoDeDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password="Janeiro.01",
            database="PeTAG"
        )
        self.cursor = self.conexao.cursor()

    def conectar(self):

        if self.conexao is None:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        return self.conexao

    # def getCoords(self, idDispositivo):
    #     self.cursor.execute(f"SELECT latitude, longitude, nomeDispositivo FROM Dispositivo WHERE idDispositivo = {idDispositivo}")
    #     return self.cursor.fetchone()
