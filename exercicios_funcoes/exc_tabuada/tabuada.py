

def tabuada_simples ():
    
        print(30*'-') 
        n = int(input('insira o numero que deseja para a tabuada : ' ))
        print(f'\ntabuada do {n}')
        print(30*'-') 
        for i in range (11):
            print(f'{n} x {i}\t= {i*n}')
    

def tabuada_completa():
        print(" tabuda completa de  0 a 10")
        for i in range ( 11 ):
            print(30*'-')    
            print(f'tabuada do {i}')
            print(30*'-') 
            for j in range(11):
                  
                print(f'{i} x {j}\t= {j*i}')
            print(30*'-')    


