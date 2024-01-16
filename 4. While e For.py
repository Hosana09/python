###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Conjectura de Collatz
###################################################

# Inicialização das variáveis

N = int(input()) #quantidade de números que terá na lista 
lista = []


# Leitura da sequência de números

for i in range(0,N):
    X = int(input()) #qual número vai ser efetuada a equação
    lista.append (X)

#print (lista)

for X in lista:
    listax = [X]
    pares = 0
    impar = 0
    Xin = X    

    while (X != 1):
        if (X % 2 == 0):
            X = X / 2
            pares = pares + 1 
        else:
            X = (3 * X) + 1
            impar = impar + 1
        listax.append(int(X))

    if (X % 2 == 0):
        pares = pares + 1 
    else:
        impar = impar + 1
        
    #print(listax)
    MAX = max(listax)

# Impressão das informações de saída

    print("Valor inicial:", Xin)
    print("Numeros Pares:", pares)
    print("Numeros Impares:", impar)
    print("Maior Numero:", MAX)

