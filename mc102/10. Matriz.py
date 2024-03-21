#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Aventura na Amazônia
#####################################################

# Criação da matriz

matriz = [['.' for _ in range(20)] for _ in range(20)]

# Leitura da entrada e preenchimento da matriz

linha, coluna = input().split() # posição inicial


# Impressão da matriz

for l in matriz:
    print(" ".join(l))
