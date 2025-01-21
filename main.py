import os
import time

#VCP final
from controller.databaseController import databaseController
from controller.userController import userController
from view.view import menu
from view.view import menu2
from view.view import menu3


#"VCP" temporario (testes)
from model.database import BancoDeDados
from model.dispositivo import Dispositivo
from model.user import User
from view.view import configuracaoConta

from dao.userDAO import userDAO



# teste = userDAO(True)
# db = BancoDeDados()




def main():
    global user_controller
    escolha = ''
    user1 = None
    database_controller = databaseController()

    while True:
        
        menu()
        
        escolha = int(input("DIGITE UMA OPÇÃO: "))

        if escolha == 1:

            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            telefone = input("Digite seu telefone: ")

            user1 = User(1,nome,email,senha,telefone)

            user_controller = userController(user1)

            verificao = user_controller.adicionarUsuario(user1)

            if verificao == False:
                break

            time.sleep(5)

        elif escolha == 2:

            while True:

                if not user1:

                    menu3()

                    userId = input("DIGITE SEU ID DE USUARIO: ")
                    userSenha = input("DIGITE SUA SENHA: ")

                    dados = database_controller.verificacao(userId,userSenha)

                    if dados:
                        
                        print("ACESSO PERMITIDO :)")
                        time.sleep(2)

                        user1 = User(dados[0],dados[1],dados[2],dados[3],dados[4])
                        user_controller = userController(user1)    
                        break

                    elif dados == None:
                        print("ERRO,O ID DE USUARIO NAO CORRESPONDE A NENHUM ID EXISTENTE")
                        time.sleep(3)

                    elif dados == '':
                        print("ACESSO NEGADO,TENTE NOVAMENTE")
                        time.sleep(3)


        while escolha!=False:
                
                menu2()

                escolha = int(input("DIGITE UMA OPÇÃO: "))

                if escolha == 1:

                    print("OS DISPOSITIVOS CONECTADOS A BASE DE DADOS SÂO: ")
                    
                    dispositivos = database_controller.verDispositivosConectados()

                    print(dispositivos)

                    time.sleep(3)
                    
                if escolha == 2:

                    id = input("DIGITE UM ID: ")
                    
                    for i in range(0, 10000, 1):
                        database_controller.atualizarConexao()

                        print(database_controller.localizacao(id))

                        # Adicionar registroHistorico

                        database_controller.adicionarRegistro(id,database_controller.localizacao(id))
                        
                        time.sleep(0.5)

                    # resultado = db.cursor.fetchone()
                    # db.cursor.close()
                    
                    # if resultado:
                    #         idDispositivo, nomeDispositivo, latitude, longitude = resultado
                    #         dispositivo1 = Dispositivo(
                    #         idDispositivo=idDispositivo,
                    #         nomeDispositivo=nomeDispositivo,
                    #         latitude=latitude,
                    #         longitude=longitude 
                    #     )
                            
                    # for i in range(0, 1000, 1):
                        # registro = dispositivo1.getData()

                        # print(registro)
                        # db.conectar()
                        # db.cursor.execute(f"insert into HistoricoCoordenadas(idDispositivo,latitude,longitude) values({registro[0]}, {registro[2]}, {registro[3]})")
                        # db.cursor.close()
                        # time.sleep(0.5)
                        # db.conexao.commit()

                if escolha == 3:

                    while True:

                        configuracaoConta()

                        configuracaoContaEscolha = int(input("DIGITE SUA ESCOLHA : "))

                        if configuracaoContaEscolha == 1:

                            novaSenha = input("Digite a senha nova: ")
                            user_controller.mudarSenha(novaSenha)

                            print("Atualizando senha...")
                            time.sleep(3)
                        
                        elif configuracaoContaEscolha == 2:

                            novoEmail = input("Digite seu novo email: ")
                            user_controller.mudarEmail(novoEmail)
                            print("Atualizando Email...")
                            time.sleep(3)
                        elif configuracaoContaEscolha == 3:
                            break

                        else:
                            print("ESCOLHA INVALIDA")
                            time.sleep(2)
                            break


                if escolha == 4:
                    break

                # if escolha == 5:
                #     print(user1.userId)
                #     print(user1.email)
                #     print(user1.nome)
                #     print(user1.senha)
                #     time.sleep(2)

if __name__ == "__main__":
    main()