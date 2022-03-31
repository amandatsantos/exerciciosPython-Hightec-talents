database = {}

def mostrar_registros ():
    if len(database) == 0:
        print(' \nbanco de dados esta vazio, Não existe nenhum registro \n')
    
    else: 
        for registro in database:
            print('-'*30)
            buscar_registro(registro)
            print('-'*30)

def buscar_registro(registro):
    if registro not in database:
        print(f' \n registro de  : {registro} não foi encontrado na base de dados  \n')
    else:
        print('-'*30)
        print('Nome:', registro)
        print('telefone:', database[registro]['telefone'])
        print('endereco:', database[registro]['endereco'])
        print('email:', database[registro]['email'])
        print('data_nascimento:', database[registro]['data_nascimento'])
        print('-'*30)


def adicionar_editar_registro (registro, telefone, endereco, email, data_nascimento ):
    
    database[registro] = {
        'telefone': telefone,
        'endereco': endereco,
        'email': email,
        'data_nascimento': data_nascimento,
    }

    print(f"\n ------- registro de {registro} incluido com sucesso !! ------- \n")

def excluir_registro(registro):
    if registro in database :
        database.pop(registro)
        print(f'\n ------ o registro de {registro} foi excluido com sucesso ----- \n')
    else: 
        print(f'\nregistro não encontrado {registro}\n')
    
    

def salvar_registro_arquivo ():
    try : 
        with open ('exercicios_funcoes/exc_cadastro/repositorio_registros/registros.txt', 'a') as arq:
            arq.writelines ("registro\t | telefone\t | endereco\t | email\t | data_nascimento\n")
            for registro in database:
                telefone = database[registro]['telefone']
                endereco = database[registro]['endereco']
                email = database[registro]['email']
                data_nascimento = database[registro]['data_nascimento']
                
                arq.writelines (f'{registro}\t\t | {telefone}\t\t | {endereco}\t\t | {email}\t\t | {data_nascimento}\n')
            print('---- registros salvos em arquivo com sucesso !!! ')

            
    except KeyError as error :
            print(f" ----- erro !!! ocorreu algum erro ao salrvar aquivo dos registros  {error}!!")