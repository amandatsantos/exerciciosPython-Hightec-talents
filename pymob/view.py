import controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")


criarArquivos(
    "categoria.txt", "inquilino.txt",
    "imovel.txt", "aluguel.txt",
    "corretor.txt", "proprietario.txt")



if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                          "Digite 2 para acessar ( Imovel )\n"
                          "Digite 3 para acessar ( Proprietario )\n"
                          "Digite 4 para acessar ( Inquilino )\n"
                          "Digite 5 para acessar ( Corretores )\n"
                          "Digite 6 para acessar ( Aluguel )\n"
                          
                          "Digite 8 para sair\n"))

        if local == 1:
            cat = controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar\n")
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja remover\n")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a categoria que deseja alterar\n")
                    novaCategoria = input("Digite a categoria para qual deseja alterar\n")
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break

        elif local == 2:
            cat = controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um Imovel\n"
                                    "Digite 2 para remover um Imovel\n"
                                    "Digite 3 para alterar um Imovel\n"
                                    "Digite 4 para ver o imovel\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("digite um titulo para o imovel:\n")
                    logradouro = input("Digite o logradouro: \n")
                    cep = input("Digite o cep: \n")
                    bairro = input("Digite o bairro: \n")
                    cidade = input("Digite a cidade: \n")
                    estado = input("Digite a cidade: \n")
                    valor = input("Digite o valor do aluguel : \n")
                    descricao = input("Digite uma breve descrição sobre o imovel: \n")
                    categoria = input("digite a categoria do imocel : apartamento, casa, tapera ....")
                    disponivel = input("digite se o imovel esta apto para ser alugado")
                    disponibilidade = input("digite se o imovel esta apto para ser alugado")
                    cat.cadastrarImovel(id,nome,logradouro,cep, bairro, cidade, estado, valor, descricao,  categoria, disponivel, disponibilidade)

                elif decidir == 2:
                    id= input("Digite o id do imovel que deseja remover: \n")

                    cat.removerImovel(id)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do imovel que deseja alterar: \n")
                    novoNome = input("Digite o novo nome do imovel: \n")
                    novologradouro = input("Digite o logradouro: \n")
                    novoCep = input("Digite o cep: \n")
                    novoBairro = input("Digite o bairro: \n")
                    novaCidade = input("Digite a cidade: \n")
                    novoEstado = input("Digite a estado: \n")
                    novoValor = input("Digite o novo valor do aluguel do imovel: \n")
                    novaDescricao = input("Digite uma breve descrição sobre o imovel: \n")
                    novaCategoria = input("Digite a nova categoria do imovel: \n")
                    nDisponivel = input("digite se o imovel esta apto para ser alugado")
                    disponibilidade = input("alguma observação em relação a disponibilidade:")
                    

                    cat.alterarImovel(nomeAlterar, novoNome,novologradouro, novoCep, novoBairro, novaCidade , novoEstado, novoValor, novaDescricao,novaCategoria,nDisponivel, disponibilidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break

        elif local == 3:
            cat = controller.ControllerProprietario()
            while True:
                decidir = int(input("Digite 1 para cadastrar um proprietario\n"
                                    "Digite 2 para remover um proprietario\n"
                                    "Digite 3 para alterar um proprietario\n"
                                    "Digite 4 para mostrar proprietarios\n"
                                    "Digite 5 para sair"))

                if decidir == 1:
                    nome = input("Digite o nome do proprietario: \n")
                    cpf = input("Digite o cpf do proprietario: \n")
                    telefone = input("Digite o telefone do proprietario: \n")
                    email = input("digite o email : \n")
                    categoria = input("Digite a categoria do imovel do proprietario : \n")
                    cat.cadastrarProprietario(id,nome, cpf, telefone,email, categoria)
                elif decidir == 2:
                    proprietario = input("Digite o proprietario que deseja remover: \n")
                    cat.removerProprietario(proprietario)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do proprietario que deseja alterar: \n")
                    novoNome = input('Digite o novo nome do proprietario: \n')
                    novoCpf = input('Digite o novo cpf do proprietario: \n')
                    novoTelefone = input('Digite o novo telefone do proprietario: \n')
                    novoCategoria = input('Digite a nova categoria  do imovel do proprietario: \n')

                    cat.alterarProprietario(id,nomeAlterar, novoNome, novoCpf, novoTelefone, novoCategoria)
                elif decidir == 4:
                    cat.mostrarProprietario()
                else:
                    break

        elif local == 4:
            cat = controller.ControllerInquilino()
            while True:
                decidir = int(input("Digite 1 para cadastrar um Inquilino\n"
                                    "Digite 2 para remover um Inquilino\n"
                                    "Digite 3 para alterar um Inquilino\n"
                                    "Digite 4 para mostrar Inquilinos\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do Inquilino: \n")
                    telefone = input("Digite o telefone do Inquilino: \n")
                    cpf = input("Digite o cpf do Inquilino: \n")
                    email = input("Digite o email do Inquilino: \n")
                    

                    cat.cadastrarinquilino(id,nome, telefone, cpf, email)
                elif decidir == 2:
                    inquilino = input("Digite o Inquilino que deseja remover: \n")

                    cat.removerInquilino(inquilino)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do Inquilino que deseja alterar: \n")
                    novoNome = input("Digite o novo nome do Inquilino: \n")
                    novoTelefone = input("Digite o novo telefone do Inquilino: \n")
                    novoCpf = input("Digite o novo cpf do Inquilino: \n")
                    novoEmail = input("Digite o novo email do Inquilino: \n")
                   
                    cat.alterarInquilino(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail)
                elif decidir == 4:
                    cat.mostrarInquilino()
                else:
                    break

        elif local == 5:
            cat = controller.ControllerCorretor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um Corretor\n"
                                    "Digite 2 para remover um Corretor\n"
                                    "Digite 3 para alterar um Corretor\n"
                                    "Digite 4 para mostrar Corretor\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    creci= input("Digite a clt do Corretor: \n")
                    nome = input("Digite o nome do Corretor: \n")
                    telefone = input("Digite o telefone do Corretor: \n")
                    cpf = input("Digite o cpf do Corretor: \n")
                    email = input("Digite o email do Corretor: \n")
                    

                    cat.cadastrarcorretor(creci, nome, telefone, cpf, email)
                elif decidir == 2:
                    corretor = input("Digite o corretor que deseja remover: \n")
                    cat.removerCorretor(corretor)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do corretor que deseja alterar: \n")
                    novoCreci = input("Digite a nova creci do corretor: \n")
                    novoNome = input("Digite o novo nome do corretor: \n")
                    novoTelefone = input("Digite o novo telefone do corretor: \n")
                    novoCpf = input("Digite o novo cpf do corretor: \n")
                    novoEmail = input("Digite o novo email do corretor: \n")
                   
                    cat.alterarCorretor(nomeAlterar, novoCreci, novoNome, novoTelefone, novoCpf, novoEmail)

                elif decidir == 4:
                    cat.mostrarCorretor()
                else:
                    break

        elif local == 6:
            cat = controller.ControllerAluguel()
            while True:
                decidir = int(input("Digite 1 para realizar aluguel\n"
                                    "Digite 2 para ver os alugueis\n"
                                    "Digite 3 para sair\n"))

                if decidir == 1:
                    nome = input('Digite o nome do imovel: \n')
                    proprietario = input('Digite nome do corretor: \n')
                    corretor = input('Digite nome do corretor: \n')
                    inquilino = input('Digite o nome do Inquilino: \n')
                    valor = input('Digite a quantidade: \n')
                    disponivel = False
                    cat.cadastrarImovel(id,nome, proprietario, corretor, inquilino,disponivel)
                elif decidir == 2:
                    AluguelID = input("Digite o id do imovel: \n")
                    cat.mostrarVenda(AluguelID)

        elif local == 7:
            a = controller.ControllerAluguel()
            
        else:
            break