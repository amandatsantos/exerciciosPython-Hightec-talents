#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


while True : 
    print("+"*80,'\n')
    print(f"\t\tCelsius em  Fahrenheit\n\n-> não utilize letras ou caracteres especiais no valor que dejesa ser convertido. <-\n")
    celsius= float(input("insira a entrada -  Celsius: "))
    fahrenheit = (celsius *1.8) + 32
    print("\na conversão de Celsius em  Fahrenheit  é dada por : °F = °C x 9 ÷ 5 + 32\n")
    print("+"*80,'\n')
    print(f"conversão : {celsius} °C = {round(fahrenheit,2)} °F")