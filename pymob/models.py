from datetime import datetime
class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Imovel (object):
    #gerar o id
    ref_id = 0
    def __init__(self, id,nome,logradouro, cep, bairro, cidade, estado, valor, descricao, categoria, disponivel = True):
        Imovel.ref_id += 1
        self.id = Imovel.ref_id
        self.nome = nome
        self.logradouro = logradouro
        self.cep= cep
        self.bairro= bairro
        self.cidade= cidade
        self.estado=estado
        self.valor= valor
        self.descricao = descricao
        self.categoria = categoria
        self.disponivel = disponivel

class Estoque:
    def __init__(self, imovel: Imovel, diponivel= True):
        self.imovel = imovel
        self.disponivel= diponivel

class Aluguel:
    ref_id = 0
    def __init__(self, id, imovelAlugado:Imovel, proprietario,corretor, inquilino, data = datetime.now().strftime("%d/%m/%Y")):
        Aluguel.ref_id += 1
        self.id = Aluguel.ref_id
        self.imovelAlugado = imovelAlugado
        self.proprietario = proprietario
        self.corretor = corretor
        self.inquilino= inquilino
        self.data = data

class Proprietario:
    ref_id = 0
    def __init__(self, id, nome, cpf, telefone, email, categoria):
        Proprietario.ref_id += 1
        self.id = Proprietario.ref_id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.categoria = categoria

class Pessoa:
    ref_id = 0
    def __init__(self, id, nome, telefone, cpf, email):
        Pessoa.ref_id += 1
        self.id = Pessoa.ref_id
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        

class Corretor(Pessoa):
    ref_id = 0
    def __init__(self, id,creci, nome, telefone, cpf, email):
        Corretor.ref_id += 1
        self.id = Corretor.ref_id
        self.creci = creci
        super(Corretor, self).__init__(id,nome, telefone, cpf, email)