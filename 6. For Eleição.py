###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Eleição 2022
###################################################

# Leitura no número de candidatos
numero_candidatos = int(input())

# Leitura do nome dos candidatos
nome_candidatos = []
for i in range(0, numero_candidatos):
    nome = input()
    nome_candidatos.append(nome)

# Leitura dos votos
quantidade_votos = []
for n in range(0, numero_candidatos+2):
    votos = int(input())
    quantidade_votos.append(votos)
    
max_votos = max(quantidade_votos[0:-2])
posicao_max = quantidade_votos.index(max_votos)
vencedor = nome_candidatos[posicao_max]
total_votos_validos = sum(quantidade_votos [:-2])



# Impressão das informações de saída

if max_votos >= total_votos_validos // 2:
# Se houve vencedor em primeiro turno
    print(vencedor, "foi o vencedor da eleição")
else:
# Se é necessário segundo turno
    print("Haverá segundo turno entre:")
    primeiro = vencedor
    lista_por_ordem = quantidade_votos.copy()
    lista_por_ordem.sort(reverse=True)
    segundo = nome_candidatos[quantidade_votos.index(lista_por_ordem[1])]
    print(primeiro)
    print(segundo)



total_votos = sum(quantidade_votos)
print("Total de votos:", total_votos)

print("Votos válidos:", total_votos_validos)
