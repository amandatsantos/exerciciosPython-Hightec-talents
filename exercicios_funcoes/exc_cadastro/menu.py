from registro import *

usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario} !\n")

while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar")
    print("2 - mostrar registros")
    print("3 - buscar registro")
    print("4 - editar registro")
    print("5 - excluir_registro")
    print("6 - salvar em arquivo os registos")
    print(" 7 - sair")

    opcao = int(input(""))
    if opcao in [1,2,3,4,5,6, 7]:
        if opcao == 1: #Cadastrar
            registro = input("insira o nome do registro que deseja adicionar:\n ")
            while registro == "":
                    registro = input("Coloque o nome: ")
            try: 
                database [ registro]
                print(f' --- registro com esse nome {registro} já existe')
            except :
                telefone = ""
                endereco = ""
                email = ""
                data_nascimento = ""
                
                while telefone == "":
                    telefone= input("Coloque o telefone: ")
                while endereco == "":
                    endereco = input("Coloque o endereço: ")
                while email == "":
                    email = input("Coloque o email: ")
                while data_nascimento == "":
                    data_nascimento = input("Coloque a data nascimento: ")

            adicionar_editar_registro(registro, telefone, endereco, email,data_nascimento)
            
            
        elif opcao == 2: #mostrar registros
            mostrar_registros()
            
        elif opcao == 3:#buscar registros
            registro = input('insira o nome do registro para a busca:\n ')
            buscar_registro(registro)

        elif opcao == 4:# editar registro
            registro = input("insira o nome do registro que deseja alterar: ")
            while registro == "":
                    registro = input("Coloque o nome: ")
            try: 
                database [ registro]
                print(f' --- editando o registro identificado como : {registro} ')
            
                while True:
                    startar = input("\naqui o registro ira ser sobre-escrito, tenha certeza antes de atualiza-lo ... pressione enter para continuar\n")
                    opcao  = int(input("\ndeseja continuar e atualizar registro? -aperte - 1\ndeseja sair da opcao editar contato ?- aperte - 2 \n"))
                    if opcao == 1: 
                        
                        telefone = ""
                        endereco = ""
                        email = ""
                        data_nascimento = ""
                        
                        while telefone == "":
                            telefone= input("Coloque o telefone: ")
                        while endereco == "":
                            endereco = input("Coloque o endereço: ")
                        while email == "":
                            email = input("Coloque a email: ")
                        while data_nascimento == "":
                            data_nascimento = input("Coloque a data de nascimento: ")
                        adicionar_editar_registro(registro, telefone, endereco, email,data_nascimento)
                    elif opcao == 2 :
                        print(" \natualização/edição não confirmada, voltando para o menu inicial\n")
                        break
                    else:
                        ('opção invalida')
            except KeyError:
                    print("\nregistro não existe na base de dados\n")
                    
                

        elif opcao == 5: # excluir registro
            
            registro = input('insira o nome do registro que deseja excluir:\n ')
            excluir_registro(registro)
        
        elif opcao == 6: # salvar arquiv
            salvar_registro_arquivo()

        elif opcao == 7:#Sair        
            print("Saindo do sistema...")
            break
    else:
        print("Opção Inválida!")