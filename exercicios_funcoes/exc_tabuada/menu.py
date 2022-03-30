from tabuada import  tabuada_completa, tabuada_simples



while True:
    start = input("\naperte a tecla enter para começar ... \n")
   
    print("\nSelecione uma opção:\n\n")
    print("1 - tabuada de um numero especifico ")
    print("2 - tabuada completa")
    print("3 - Sair\n\n")
    
    opcao = int(input(""))
    if opcao in [1,2,3]:
                
        if opcao == 1:#tabuada
            tabuada_simples()
            
        elif opcao == 2:#tabuada
            
            tabuada_completa()

        elif opcao == 3:#Sair
            print("Saindo do sistema...")
            break
    else:
        print("Opa, Opção Inválida!")