from models import *
from dao import  *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso')
        else:
            print('A categoria que deseja cadastrar já existe')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Imovel(x.imovel.nome, x.imovel.valor, "Sem categoria"), x.disponivel) if(x.imovel.categoria == categoriaRemover) else(x), estoque))
        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines("\n")

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x) ,x))
                print('A altereção foi efetuada com sucesso')

                estoque = DaoEstoque.ler()

                estoque = list(map(
                    lambda x: Estoque(Imovel(x.imovel.nome, x.imovel.valor, categoriaAlterada), x.disponivel) if (
                                x.imovel.categoria == categoriaAlterar) else (x), estoque))
                with open('estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.imovel.nome + "|" + i.imovel.valor + "|" + i.imovel.categoria + "|" + str(
                            i.disponivel))
                        arq.writelines("\n")

            else:
                print("A categoria para qual deseja alterar já existe")

        else:
            print('A categoria que deseja alterar não existe')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia!')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

###############

class ControllerEstoque:
    def cadastrarImovel(self, id, logradouro, cep, bairro, cidade, estado, valor, descricao, disponivel, categoria):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.imovel.logadouro == logradouro, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Imovel(logradouro, valor, categoria)
                DaoEstoque.salvar(produto,disponivel)
                print('Imovel cadastrado com sucesso')
            else:
                print('Imovel já existe em estoque')
        else:
            print('Categoria inexistente')

    def removerProduto(self, logradouro):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.imovel.logradouro == logradouro, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].imovel.logradouro == logradouro:
                    break
            print('Imovel foi removido com sucesso')
        else:
            print('O Imovel que deseja remover não existe')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.imovel.nome + "|" + i.imovel.valor + "|" +
                           i.imovel.categoria + "|" + str(i.disponivel))
                arq.writelines('\n')

    def alterarImovel(self, nomeAlterar, novoNome, novoValor, novaCategoria, disponibilidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.imovel.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.imovel.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Imovel(novoNome, novoValor, novaCategoria), disponibilidade) if(x.imovel.nome == nomeAlterar) else(x), x))
                    print('imovel alterado com sucesso')
                else:
                    print('imovel já cadastro')
            else:
                print('Imovel que deseja alterar não existe')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines( i.imovel.id +"|" + i.imovel.nome + "|" + i.imovel.logradouro + "|" + i.imovel.cep +"|" +i.imovel.bairro+ "|" + i.imovel.cidade + "|" + i.imovel.estado +  "|" + i.imovel.valor +"|" +
                           + "|" + i.imovel.descricao +"|"+i.imovel.categoria + "|" + str(i.disponivel))
                    arq.writelines('\n')
        else:
            print('A categoria informada não existe')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            print("==========Produtos==========")
            for i in estoque:
                print(f"Nome: {i.imovel.nome}\n"
                    f"logradouro: {i.imovel.logradouro}\n"
                    f"bairro: {i.imovel.bairro}\n"
                    f" cidade: {i.imovel. cidade}\n"
                    f" estado: {i.imovel. estado}\n"
                      f"Preco: {i.imovel.valor}\n"
                      f"Categoria: {i.imovel.categoria}\n"
                      f"Quantidade: {i.disponibilidade}"

                )
                print("--------------------")

class ControllerAluguel:
    def cadastrarImovel(self, nomeImovel, corretor, proprietario, inquilino, disponivel):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        disponibilidade = False
        for i in x:
            if existe == False:
                if i.imovel.nome == nomeImovel:
                    existe = True
                    if i.disponibilidade == disponivel:
                        disponibilidade = True
                        alugado = Aluguel(Imovel(i.imovel.id, i.imovel.nome, i.imovel.logradouro,i.imovel.cep, i.imovel.bairo, i.imovel.cidade,i.imovel.estado,i.imovel.valor, i.imovel.descricao,i.imovel.categoria ), corretor, proprietario, inquilino, disponibilidade)

                        
                        alugueldispo = True
                        DaoAluguel.salvar(alugado)

            temp.append(Estoque(Imovel(i.imovel.id, i.imovel.nome, i.imovel.logradouro,i.imovel.cep, i.imovel.bairo, i.imovel.cidade,i.imovel.estado,i.imovel.valor, i.imovel.descricao,i.imovel.categoria), i.disponibilidade))

        arq = open('estoque.txt', 'w')
        arq.write("")


        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

        if existe == False:
            print('O imovel com esse nome  nao exite')
            return None
        elif not disponivel:
            print('o imovel não esta disponivel para alugar')
            return None
        else:
            print('aluguel realizado com sucesso')
            return alugueldispo



    def mostrarVenda(self, id):
            x = DaoAluguel.ler()
            
            AluguelID = list(filter(lambda x: x.id == id, x))

            if len(AluguelID) > 0:
                for i in range(len(x)):
                     if x[i].id == id:
                        print(f"=========alugueis==========")
                        print(
                            f"Nome: {i.imovel.nome}\n"
                                f"logradouro: {x[i].imovel.logradouro}\n"
                                f"bairro: {x[i].imovel.bairro}\n"
                                f" cidade: {x[i].imovel. cidade}\n"
                                f" estado: {x[i].imovel. estado}\n"
                                f"Preco: {x[i].imovel.valor}\n"
                                f"Categoria: {x[i].imovel.categoria}\n"
                                f"Quantidade: {x[i].disponibilidade}")
                  
            else:
                print('registro  não encontrado')


class ControllerProprietario:
    def cadastrarProprietario(self, id, nome, cpf, telefone, categoria):
        x = DaoProprietario.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaTelefone = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print("O cpf já existe")
        elif len(listaTelefone) > 0:
            print('O telefone já existe')
        else:
            if len(cpf)  == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoProprietario.salvar(Proprietario(id,nome, cpf, telefone, categoria))
            else:
                print("Digite um cpf ou telefone válido")

    def alterarProprietario(self, nomeAlterar, novoNome, novoCpf, novoTelefone, novoCategoria):
        x = DaoProprietario.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCpf, x))
            if len(est) == 0:
                x = list(map(lambda x: Proprietario(novoNome, novoCpf, novoTelefone, novoCategoria) if(x.nome == nomeAlterar) else(x),x))
            else:
                print('Cpf já existe')
        else:
            print('O Propprietario que deseja alterar nao existe')

        with open('proprietario.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cpf + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines('\n')
            print('fornecedor alterado com sucesso')

    def removerProprietario(self, nome):
        x = DaoProprietario.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('O Proprietario que deseja remover não existe')
            return None

        with open('proprietario.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cpf + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines('\n')
            print('Proprietario removido com sucesso')

    def mostrarProprietario(self):
        proprietario = DaoProprietario.ler()
        if len(proprietario) == 0:
            print("Lista de proprietarios vazia")

        for i in proprietario:
            print("=========proprietario==========")
            print(f"Categoria de imovel: {i.categoria}\n"
                  f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Cpf: {i.cnpj}")

class ControllerInquilino:
    def cadastrarinquilino(self, id, nome, telefone, cpf, email):
        x = DaoPessoa.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('CPF já existente')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email))
                print('inquilino Cadastrado com sucesso')
            else:
                print('digite um cpf ou telefone válido')

    def alterarInquilino(self, id,nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.id == id, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(id, novoNome, novoTelefone, novoCpf, novoEmail) if (
                        x.id == id) else (x), x))
        else:
            print('O cliente que deseja alterar nao existe')

        with open('inquilino.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('cliente alterado com sucesso')

    def removerCliente(self, nome):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('O inquilino que deseja remover não existe')
            return None

        with open('inquilino.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('inquilino removido com sucesso')

    def mostrarInquilino(self):
        inquilino = DaoPessoa.ler()

        if len(inquilino) == 0:
            print("Lista de clientes vazia")

        for i in inquilino:
            print("=========inquilino=========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Endereço: {i.endereco}\n"
                  f"Email: {i.email}\n"
                  f"CPF: {i.cpf}")

class ControllerCorretor:
    def cadastrarcorretor(self, id,  creci, nome, telefone, cpf, email, endereco):
        x = DaoCorretor.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaCreci = list(filter(lambda x: x.creci == creci, x))
        if len(listaCpf) > 0:
            print('CPF já existente')
        elif len(listaCreci) > 0:
            print('Já existe um corretor com essa creci')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DaoCorretor.salvar(Corretor(creci, nome, telefone, cpf, email))
                print('Funcionario Cadastrado com sucesso')
            else:
                print('digite um cpf ou telefone válido')

    def alterarCorretor(self, nomeAlterar, novoCreci, novoNome, novoTelefone, novoCpf, novoEmail):
        x = DaoCorretor.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Corretor(novoCreci,novoNome, novoTelefone, novoCpf, novoEmail) if (
                    x.nome == nomeAlterar) else (x), x))
        else:
            print('O funcionario que deseja alterar nao existe')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.creci + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email
                              )
                arq.writelines('\n')
            print('funcionario alterado com sucesso')

    def removerCorretor(self, nome):
        x = DaoCorretor.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('O Corretor que deseja remover não existe')
            return None

        with open('corretor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Corretor removido com sucesso')

    def mostrarCorretor(self):
        corretor = DaoCorretor.ler()

        if len(corretor) == 0:
            print("Lista de corretor vazia")

        for i in corretor:
            print("========Funcionario==========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Email: {i.email}\n"
                  f"Endereço: {i.endereco}\n"
                  f"CPF: {i.cpf}\n"
                  f"Creci: {i.creci}\n")


