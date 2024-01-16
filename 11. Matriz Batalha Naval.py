#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Batalha Naval
#####################################################

# Leitura da matriz

matriz = []
for _ in range(10):
    matriz.append(input().split())

navios = {}
for l in matriz:
    for c in l:
        if (c != "."):
            if (c not in navios):
                navios[c] = 0
            
            navios[c] = navios[c] +  1
    
# Leitura e processamento dos palpites
dic_linha = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

n_palpites = int(input())

for n in range (n_palpites):
    linha, coluna = input().split()
    linha = dic_linha[linha]
    coluna = int(coluna) - 1
    resultado = matriz [linha][coluna]
    if (resultado == "."):
        print("agua")
    else:
        navios[resultado] -= 1
        qtd = navios[resultado]
        if (qtd > 0):
            print("atingiu o navio " + resultado)
        else:
            print("afundou o navio " + resultado)        

# Dica: Você pode usar um dicionario para gravar quantas
# partes de um navio ainda devem ser atingidas para afundá-lo
