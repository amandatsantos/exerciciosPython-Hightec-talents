#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

while True:
    print("/"*80,'\n')
    print(f"\t\tArea de um quadrado e o seu dobro \n\n-> não utilize letras ou caracteres especiais no valor que dejesa ser calculado. <-\n")
    print("informe a medida de um dos lados do quadrado ")
    lado = float(input("insira o valor : "))
    area =  lado **2
    area_dobro = area**2
    print(f"\na área do quadrado é {area} m²/cm² e o dobro da área do quadrado é {area_dobro} m²/cm²\n")
 