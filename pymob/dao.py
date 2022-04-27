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

#x = Imovel(id, "casa 2 quartos ", 'rua lar nova esperança', '45700-00', 'nova itapetinga', 'itapetinga', 'bahia', '214560', 'casa copm varanda e garagem', 'apartamento') 
a = Aluguel(id , "lidalvo", 'jose', 'joao')
DaoAluguel.salvar(a) 

class DaoImovel:
    @classmethod
    def salvar(cls,imovel: Imovel, disponibilidade):
        with open('imovel.txt', 'a') as arq:
            arq.writelines(str(imovel.id)+"|" + imovel.nome + "|" + imovel.logradouro + "|" + imovel.cep +"|" + imovel.bairro+ "|" + imovel.cidade + "|" + imovel.estado + "|" + str(imovel.valor) +"|"+imovel.descricao +"|"+imovel.categoria + "|" + imovel.disponivel +"|"+ disponibilidade)
            arq.writelines('\n')



    @classmethod
    def ler(cls):
        with open('imovel.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Imovel(i[0],i[1], i[2], i[3], i[4],i[5],i[6],i[7],i[8],i[9],i[10]),i[11]))

        return est

a = Estoque(id, ' casa no lago', ' bosque', '12365478', 'bairro de oz', 'cidadede oz', ' estado de oz', '123654', ' lago de oz proximo a casa', 'casa', 'sim', "sim")
DaoImovel.salvar(a)

class DaoProprietario:
    @classmethod
    def salvar(cls, proprietario : Proprietario):
        with open('proprietario.txt', 'a') as arq:
            arq.writelines(str(proprietario.id)+"|"+proprietario.nome + "|" + proprietario.cpf + "|" + proprietario.telefone +"|"+ proprietario.email
                           + "|" + proprietario.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('proprietario.txt', 'r') as arq:
            cls.proprietario = arq.readlines()

        cls.proprietario = list(map(lambda x: x.replace('\n', ''), cls.proprietario))
        cls.proprietario = list(map(lambda x: x.split('|'), cls.proprietario))
        prop = []
        for i in cls.proprietario:
            prop.append(Proprietario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return prop
a =Proprietario(id,'joao' , '12365478912', "1236547891", "amanama@amana",'casa')
DaoProprietario.salvar(a)
 
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('inquilino.txt', 'a') as arq:
            arq.writelines(str(pessoas.id) +"|"+pessoas.nome + "|" + pessoas.telefone +"|" + pessoas.email + "|" + pessoas.cpf
                           )
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
a = Pessoa(id, 'luan', '123647895', '5465464564', 'amaanaamana@amnaman')
DaoPessoa.salvar(a) 


class DaoCorretor:
    @classmethod
    def salvar(cls, corretor: Corretor):
        with open('corretor.txt', 'a') as arq:
            arq.writelines(str(corretor.id)+"|"+corretor.creci + "|" + corretor.nome + "|" + corretor.telefone
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
            corret.append(Corretor(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        return corret

p= Corretor(id, 'BA-123654', "jose", "14563214565", "123654978", 'asdasdas')        
DaoCorretor.salvar(p) 