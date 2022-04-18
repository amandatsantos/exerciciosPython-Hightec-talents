from models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat

DaoCategoria.salvar("apartamento")


class DaoAluguel:
    @classmethod
    def salvar(cls, aluguel: Aluguel):
        with open('aluguel.txt', 'a') as arq:
            arq.writelines(str(aluguel.id)+"|"+aluguel.imovelAlugado.nome + "|" + aluguel.imovelAlugado.valor + "|" +
                           aluguel.imovelAlugado.categoria + "|" + aluguel.proprietario + "|" +aluguel.corretor + "|" +aluguel.inquilino +"|" + aluguel.data)
                           
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('aluguel.txt', 'r') as arq:
            cls.aluguel = arq.readlines()

        cls.aluguel = list(map(lambda x: x.replace('\n', ''), cls.aluguel))
        cls.aluguel = list(map(lambda x: x.split('|'), cls.aluguel))
        alug = []
        for i in cls.aluguel:
            alug.append(Aluguel(Imovel(i[0], i[1], i[2]), i[3], i[4], i[5], i[6], i[7]))
        return alug

x = Imovel(id, "casa 2 quartos ", 'rua lar nova esperança', '45700-00', 'nova itapetinga', 'itapetinga', 'bahia', '214560', 'casa copm varanda e garagem', 'apartamento')

a = Aluguel(id ,x, "lidalvo", 'jose', 'joao')
DaoAluguel.salvar(a)

class DaoEstoque:
    @classmethod
    def salvar(cls,imovel: Imovel, disponivel):
        with open('estoque.txt', 'a') as arq:
            arq.writelines( imovel.id +"|" + imovel.nome + "|" + imovel.logradouro + "|" + imovel.cep +"|" + imovel.bairro+ "|" + imovel.cidade + "|" + imovel.estado +  "|" + imovel.valor +"|" +
                           + "|" + imovel.descricao +"|"+imovel.categoria + "|" + (imovel.disponivel))
            arq.writelines('\n')



    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Imovel(i[0], i[1], i[2], i[3], i[4],i[5],i[6],i[7],i[8],i[9], i[10]), str(i[10])))

        return est
b = Imovel(id,"casa 3 quartos", 'rua 25','45700000', "nova itapetinga", 'itapetinga', "bahia", "2.500", ' casa arejada', 'apartamento',)
DaoEstoque.salvar(b)
class DaoProprietario:
    @classmethod
    def salvar(cls, propietario : Proprietario):
        with open('proprietario.txt', 'a') as arq:
            arq.writelines(propietario.nome + "|" + propietario.cpf + "|" + propietario.telefone
                           + "|" + propietario.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('proprietario.txt', 'r') as arq:
            cls.proprietario = arq.readlines()

        cls.proprietario = list(map(lambda x: x.replace('\n', ''), cls.proprietario))
        cls.proprietario = list(map(lambda x: x.split('|'), cls.proprietario))
        prop = []
        for i in cls.proprietarios:
            prop.append(Proprietario(i[0], i[1], i[2], i[3]))

        return prop



class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('inquilino.txt', 'a') as arq:
            arq.writelines(pessoas.id +"|"+pessoas.nome + "|" + pessoas.telefone + "|" + pessoas.cpf
                           + "|" + pessoas.email )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('inquilino.txt', 'r') as arq:
            cls.inquilino = arq.readlines()

        cls.inquilino = list(map(lambda x: x.replace('\n', ''), cls.inquilino))
        cls.inquilino = list(map(lambda x: x.split('|'), cls.inquilino))

        inqui = []
        for i in cls.inquilino:
            inqui.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return inqui


class DaoCorretor:
    @classmethod
    def salvar(cls, corretor: Corretor):
        with open('corretor.txt', 'a') as arq:
            arq.writelines(corretor.id+"|"+corretor.creci + "|" + corretor.nome + "|" + corretor.telefone
                           + "|" +corretor.cpf + "|" + corretor.email )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('corretor.txt', 'r') as arq:
            cls.corretor= arq.readlines()

        cls.corretor= list(map(lambda x: x.replace('\n', ''), cls.corretor))
        cls.corretor = list(map(lambda x: x.split('|'), cls.corretor))

        corret = []
        for i in cls.corretor:
            corret.append(Corretor(i[0], i[1], i[2], i[3], i[4], i[5]))

        return corret