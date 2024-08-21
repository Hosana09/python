###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Conjectura de Collatz
###################################################

# Inicialização das variáveis
N = int(input("Digite a quantidade de número que terá a lista: ")) #quantidade de números que terá na lista 
lista = []


# Leitura da sequência de números
for i in range(0,N):
    X = int(input("Digite o número para ser efetuada a equação: ")) #qual número vai ser efetuada a equação
    lista.append (X)

print("A sequência para realizar a Conjectura de Collatz é:", lista)

for X in lista:
    listax = [X]
    pares = 0
    impares = 0
    Xin = X  
    if (X % 2 == 0):
        pares = pares + 1 
    else:
        impares = impares + 1

    while (X != 1):
        if (X % 2 == 0):
            X = X / 2
            pares = pares + 1 
            listax.append(int(X))
        else:
            X = (3 * X) + 1
            impares = impares + 1
            listax.append(int(X))
    
#print(listax)
    MAX = max(listax)

# Impressão das informações de saída
    print("Para o número", Xin, "temos a sequência:", listax)  
    print("Valor inicial:", Xin)
    print("Quantidade de números pares:", pares)
    print("Quantidade de números ímpares:", impares)
    print("Maior número:", MAX)