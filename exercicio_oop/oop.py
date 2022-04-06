#Fazer a herança das seguintes classes:
#MeioTransporte
#Terrestre            / Aquatico           / Aereo
#Carro / Caminhao     Remo / Barco       Avião / Helicóptero
#Use a imaginação para criar e separar os seus atributos
#Para o dia 07/04

class Transporte ():
    def __init__(self, marca, trabalho, lazer, combustivel):
        self.marca = marca
        self.trabalho = trabalho
        self.lazer = lazer
        self.combustivel = combustivel 

###############################

class Terrestre (Transporte):
    def __init__(self, marca,  trabalho, lazer, combustivel, ferroviario , quants_rodas, categoria, modelo, ano, km_rodados  ) :
        super().__init__(marca,  trabalho, lazer, combustivel)
        self.ferroviario = ferroviario
        self.quants_rodas = quants_rodas
        self.categoria = categoria
        self.modelo = modelo
        self.ano = ano
        self.km_rodados = km_rodados

class Carro (Terrestre):
    def __init__(self, marca,  trabalho, lazer, combustivel, ferroviario, quants_rodas, categoria, modelo, ano, km_rodados, sensor_estacionamento, teto_solar):
        super().__init__(marca,  trabalho, lazer, combustivel, ferroviario, quants_rodas, categoria, modelo, ano, km_rodados )
        self.sensor_estacionamento = sensor_estacionamento
        self.teto_solar = teto_solar
    def __str__(self) :
        return f'\n\n\t---- ficha carro ----\t \n\n \tMarca : {self.marca}\t \n \tUtilizada para trabalho: {self.trabalho}\t \n \tUtilizada para lazer: {self.lazer}\t \n \tTipo de Combustivel: {self.combustivel}\t \n \tFerroviario: {self.ferroviario}\t \n \tQuatidade  de rodas: {self.quants_rodas}\t \n \t categoria: {self.categoria}\t \n \tmodelo: {self.modelo}\t \n \tano: {self.ano}\t \n \tkm rodados: {self.km_rodados}\t \n \tsensor de estacioanmento: {self.sensor_estacionamento}\t \n \tteto solar: {self.teto_solar}\t \n \t \n\n' # km_rodados, capacidade_carga, frete 

class Camimhao (Terrestre):
    def __init__(self, marca,  trabalho, lazer, combustivel, ferroviario, quants_rodas, categoria, modelo, ano, km_rodados, capacidade_carga, frete ):
        super().__init__(marca,  trabalho, lazer, combustivel, ferroviario, quants_rodas, categoria, modelo, ano, km_rodados)
        self.capacidade = capacidade_carga
        self.frete = frete

    def __str__(self) :
        return f'\t---- ficha caminhao ----\t \n\n \tMarca: {self.marca}\t \n \tUtilizada para trabalho: {self.trabalho}\t \n \tUtilizada para lazer: {self.lazer}\t \n \tTipo de Combustivel: {self.combustivel}\t \n \tFerroviario: {self.ferroviario}\t \n \tQuatidade  de rodas: {self.quants_rodas}\t \n \tcategoria: {self.categoria}\t \n \tmodelo {self.modelo}\t \n \tano: {self.ano}\t \n \tkm rodados: {self.km_rodados}\t \n \tcapacidade : {self.capacidade}\t \n \tpega frete: {self.frete}\t\n \t \n\n' # km_rodados, capacidade_carga, frete 


##########################################

class Aquatico(Transporte):
    def __init__(self, marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga):
        super().__init__(marca, trabalho, lazer, combustivel)
        self.categoria = categoria
        self.modelo = modelo
        self.ano = ano
        self.porte = porte
        self.transporte_pessoas = transporte_pessoas
        self.trapostes_carga = trapostes_carga
        self.capacidade_pessoa = capacidade_pessoa
        self.capacidade_carga = capacidade_carga

class BarcoAremo(Aquatico):
    def __init__(self, marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga, motor_imbutido):
        super().__init__(marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga)
        self.motor_imbutido = motor_imbutido

    def __str__(self) :
            return f'\t---- ficha Barco a Remo ----\t \n\n \tMarca : {self.marca}\t \n \tUtilizada para trabalho: {self.trabalho}\t \n \tUtilizada para lazer: {self.lazer}\t \n \tTipo de Combustivel: {self.combustivel}\t  \n \tcategoria: {self.categoria}\t \n \tmodelo: {self.modelo}\t \n \tano: {self.ano}\t \n \tPorte: {self.porte}\t \n \ttransporta pessoa : {self.transporte_pessoas}\t \n \tTransporta Carga: {self.trapostes_carga}\t \n \tCapacidades de pessoas: {self.capacidade_pessoa}\t \n \tCapacidade de Carga: {self.capacidade_carga}\t \n \tteto solar: {self.motor_imbutido}\t \n \t \n\n' #porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, motor_imbutido

class BarcoAmotor(Aquatico):
    def __init__(self, marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga, intercontinental, tipo_comercial):
        super().__init__(marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga)
        self.intercontinental = intercontinental
        self.tipo_comercial = tipo_comercial

    def __str__(self) :
            return f'\t---- ficha Barco Motor ----\t \n\n \tMarca : {self.marca}\t \n \tUtilizada para trabalho: {self.trabalho}\t \n \tUtilizada para lazer: {self.lazer}\t \n \tTipo de Combustivel: {self.combustivel}\t \n \tcategoria: {self.categoria}\t \n \tmodelo: {self.modelo}\t \n \tano: {self.ano}\t \n \tPorte: {self.porte}\t \n \ttransporta pessoa: {self.transporte_pessoas}\t \n \tTransporta Carga: {self.trapostes_carga}\t \n \tCapacidades de pessoas: {self.capacidade_pessoa}\t \n \tCapacidade de Carga: {self.capacidade_carga}\t \n \tIntercontinental: {self.intercontinental}\t \n \tComercial: {self.tipo_comercial}\t \n \t \n\n' #intercontinental, tipo_comercial

######################################

class Aereo (Transporte):
    def __init__(self, marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga, motor):
        super().__init__(marca, trabalho, lazer, combustivel)
        self.categoria = categoria
        self.modelo = modelo
        self.ano = ano
        self.porte = porte
        self.transporte_pessoas = transporte_pessoas
        self.trapostes_carga = trapostes_carga
        self.capacidade_pessoa = capacidade_pessoa
        self.capacidade_carga = capacidade_carga
        self.motor = motor

class Helicoptero(Aereo):
    def __init__(self, marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga, motor, taxi_aereo):
        super().__init__(marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga, motor)
        self.taxi_aereo = taxi_aereo
    def __str__(self) :
            return f'\t---- ficha Helicoptero ----\t \n\n \tMarca: {self.marca}\t \n \tUtilizada para trabalho: {self.trabalho}\t \n \tUtilizada para lazer: {self.lazer}\t \n \tTipo de Combustivel: {self.combustivel}\t \n \tcategoria: {self.categoria}\t \n \tmodelo: {self.modelo}\t \n \tano: {self.ano}\t \n \tPorte: {self.porte}\t \n \ttransporta pessoa : {self.transporte_pessoas}\t \n \tTransporta Carga: {self.trapostes_carga}\t \n \tCapacidades de pessoas: {self.capacidade_pessoa}\t \n \tCapacidade de Carga: {self.capacidade_carga}\t \n \ttipo de motor: {self.motor}\t \n \tpresta serviço taxi aereo: {self.taxi_aereo}\t \n \t \n\n' #intercontinental, tipo_comercial

class Aviao (Aereo):
    def __init__(self, marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga, motor, militar):
        super().__init__(marca, trabalho, lazer, combustivel, categoria, modelo, ano, porte, transporte_pessoas, trapostes_carga, capacidade_pessoa, capacidade_carga, motor)
        self.militar = militar

    def __str__(self) :
            return f'\t---- ficha Aviao ----\t \n\n \tMarca: {self.marca}\t \n \tUtilizada para trabalho: {self.trabalho}\t \n \tUtilizada para lazer: {self.lazer}\t \n \tTipo de Combustivel: {self.combustivel}\t \n \tcategoria: {self.categoria}\t \n \tmodelo: {self.modelo}\t \n \tano: {self.ano}\t \n \tPorte: {self.porte}\t \n \ttransporta pessoa : {self.transporte_pessoas}\t \n \tTransporta Carga: {self.trapostes_carga}\t \n \tCapacidades de pessoas: {self.capacidade_pessoa}\t \n \tCapacidade de Carga: {self.capacidade_carga}\t \n \ttipo de motor: {self.motor}\t \n \tmissão qualificada: {self.militar}\t \n \t \n\n' #intercontinental, tipo_comercial

#############################
# terrestres
carro = Carro (" Volkswagen ", "não" ,"sim", "disel", 'não', "5", "Picape média", "Volkswagen Amarok" , "2021" , " 0km", "sim" ," não")

caminhao = Camimhao (" Mercedes Benz", "sim" ,"não", "disel", 'não', "5", "cavalo mecanico/ caminhaão extrapesado", "MB 2644" , "2021" , " 0km", "depende do semireboque" ," sim") 

print(carro, caminhao)


# aquaticos
remo = BarcoAremo ("HELBLING", "não", "sim", " none", "passeio", "Helbling 580", "2021", "medio", "sim", "não", "5" , "---", "não")

motor = BarcoAmotor ("Bob Hope", "sim, militar", "não","disel","Roll-on/Roll-off","USNS  Bob Hope  (T-AKR-300)","1997", "medio/grande", "não","Navio de carga de veículos da classe Bob Hope" ,"26 a 45 tripulantes",  "62.069 toneladas cheias", "sim", "não")
 
print(motor, remo)


#aereos
heli = Helicoptero("Sikorsky", "sim", 'não', "disel", "helicóptero bimotor", "Sikorsky S76 C+", "2018", "medio", "sim", "não", "2 pilotos +12 passageiros", "----", "bimotor", "sim")

avi = Aviao ("Bell-Boeing",'sim', 'não', 'hibrido', 'defesa/Aeronave de transporte', ' MV-22B','2007', 'grande', 'sim','sim','60','9 070 kg (20 000 lb) de carga interna', '2 x turbo-eixos Rolls-Royce Allison T406/AE 1107C-Liberty',' Aeronave de transporte')

print(heli, avi)

