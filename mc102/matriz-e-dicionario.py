###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Dia do Progresso I
###################################################

# lendo a matriz
M = []
L = int(input())
for _ in range(L):
    M.append(input().split())


# lendo a posição inicial
linha, coluna = (int(i) for i in input().split())


# Dica: construa um dicionário com as posições de cada par de portais
portais = {}
lista_auxiliar = ["N", "S", "L", "O", "*", "#"]

for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] not in lista_auxiliar:
            if M[i][j] in portais: #sublista 
                portais[M[i][j]].append([i,j]) #append sublista
            else:
                portais[M[i][j]] = [[i,j]] #criar lista com sublista


# verificação do caminho até Piltover
posicao_anterior = ""
posicao = M[linha][coluna]

while posicao != "*" and posicao != "#" and posicao != ".":
    if posicao in lista_auxiliar:
        M[linha][coluna] = "."
#personagem vai pra norte
    if posicao == "N": 
        linha = linha - 1
    #personagem vai pra sul
    elif posicao == "S":
        linha = linha + 1
    #personagem vai pra leste
    elif posicao == "L":
        coluna = coluna + 1
    #personagem vai pra oeste
    elif posicao == "O":
        coluna = coluna - 1
    
    else:
        p = [linha,coluna]
        p1, p2 = portais [posicao]
        if p != p1:
            linha, coluna = p1
        else:
            linha, coluna = p2

           #tratar as posições 
        if posicao_anterior == "N": 
            linha = linha - 1
        #personagem vai pra sul
        elif posicao_anterior == "S":
            linha = linha + 1
        #personagem vai pra leste
        elif posicao_anterior == "L":
            coluna = coluna + 1
        #personagem vai pra oeste
        elif posicao_anterior == "O":
            coluna = coluna - 1
    
    
    posicao_anterior = posicao
    posicao = M[linha][coluna]
    
# saída de dados
if posicao == "*":
    print('Jayce conseguiu chegar em Piltover')
else:
    print('Jayce nao conseguiu chegar em Piltover')