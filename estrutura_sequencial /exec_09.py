#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

while True : 
    print("-"*80,'\n')
    print(f"\t\tFahrenheit em  Celsius\n\n-> não utilize letras ou caracteres especiais no valor que dejesa ser convertido. <-\n")
    fahrenheit= float(input("insira a entrada - Fahrenheit: "))
    celsius = 5 * ((fahrenheit-32) / 9)
    print("\na conversão de Fahrenheit para Celsius  é dada por : C = 5 × ((F-32) ÷ 9)\n")
    print("-"*80,'\n')
    print(f"conversão : {fahrenheit} °F = {round(celsius,2)} °C")