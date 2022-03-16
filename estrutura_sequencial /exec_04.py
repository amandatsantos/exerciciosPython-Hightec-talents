#Faça um Programa que peça as 4 notas bimestrais e mostre a média.



while True:
    print(30*("=-"))
    print("insira as 4 notas bimestrais para obter a media\n")
    nota_1 = float(input(" primeira nota : "))
    nota_2 = float(input(" segunda nota  : "))
    nota_3 = float(input(" terceira nota : "))
    nota_4 = float(input(" quarta nota   : "))

    media = (nota_1 + nota_2 + nota_3 + nota_4)/4

    tabela_notas =             [
                    ['primeiro:\t ', nota_1 ],
                    ['segundo:\t ', nota_2],
                    ['terceiro:\t', nota_3 ],
                    ['quarto: \t', nota_4 ],
                    ['media:\t\t' , media]]

    print(30*("=-"))
    print("notas do bimestre e resultado da media\n")       
    
    print('periodo\t\tnota')
    for results in tabela_notas:
            periodo, nota = results
            
            print (f"\n{periodo} {nota} ")
    print(30*("=-"))        


