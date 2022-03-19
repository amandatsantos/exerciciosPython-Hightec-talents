#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

while True:
    print("\n","/"*80,'\n')
    print(f"\t\tcalculo de salario  \n\n-> não utilize letras ou caracteres especiais no valor que dejesa ser calculado. <-\n")
    print(" \n1ª - informe quanto  ganha por hora \n2ª - informe numero de horas trabalhadas no mês\n")
    valor_hora = float(input("valor hora: ")) 
    horas_mes = float(input("horas trabalhadas no mês: ")) 
    salario = valor_hora*horas_mes
    print(f'\n se você  ganha {valor_hora} e trabalha {horas_mes} horas em um mês logo o seu  salário bruto (sem descontos) é R$ {round(salario,2)} ')