#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

while True : 
    print("/"*80,'\n')
    print(f"\t\tArea de um circulo \n\n-> não utilize letras ou caracteres especiais no valor que dejesa ser calculado. <-\n")
    raio = float(input('insira o valor do raio : '))
    area = 3.1415926535898*raio**2
    print("\nformula para calcular a area do circulo : \n\n \t\t A = pi × raio² \n")
    print(f'area do circulo é : {round(area,2)} m²/cm²')
    print("/"*80,'\n')
