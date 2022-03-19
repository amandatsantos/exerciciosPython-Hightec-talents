#Faça um Programa que converta metros para centímetros.

import string


while True : 
    print("/"*80,'\n')
    print(f"\t\tMetros em Centímetros\n\n-> não utilize letras ou caracteres especiais no valor que dejesa ser convertido. <-\n")
    metros = float(input("insira a entrada - METROS (m): "))
    convert_cm =  metros/0.010000
    print("\na conversão de metros em centímetros  é dada por : cm = m / 0.010000\n")
    print("/"*80,'\n')
    print(f"conversão : {metros} m  = {convert_cm} cm")
    