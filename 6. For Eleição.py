###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Eleição 2022
###################################################

# Leitura no número de candidatos
print("Eleição 2022")
numero_candidatos = int(input("Houveram quantos candidatos para a eleição de 2022? "))

# Leitura do nome dos candidatos
nome_candidatos = []
num_candidato = 1

for i in range(0, numero_candidatos):
    nome = input("Digite o nome do(a) candidato(a) " + str(num_candidato) + ": ")
    num_candidato = num_candidato + 1
    nome_candidatos.append(nome)
#print(nome_candidatos)

# Leitura dos votos
quantidade_votos = []
posicao_candidato = 0
for n in range(0, numero_candidatos):
    votos = int(input("Digite a quantidade de votos para o(a) canditado(a) " + nome_candidatos[posicao_candidato] + ": "))
    posicao_candidato += 1
    quantidade_votos.append(votos)

brancos = int(input("Digite a quantidade de votos brancos: "))
quantidade_votos.append(brancos)

nulos = int(input("Digite a quantidade de votos nulos: "))
quantidade_votos.append(nulos)

#print(quantidade_votos)

max_votos = max(quantidade_votos[0:-2])
posicao_max = quantidade_votos.index(max_votos)
vencedor = nome_candidatos[posicao_max]
total_votos_validos = sum(quantidade_votos [:-2])

# Impressão das informações de saída
if max_votos >= (total_votos_validos // 2):
# Se houve vencedor em primeiro turno
    print(vencedor, "foi o(a) vencedor(a) da eleição!")
else:
# Se é necessário segundo turno
    primeiro = vencedor
    lista_por_ordem = quantidade_votos.copy()
    lista_por_ordem.sort(reverse=True)
    segundo = nome_candidatos[quantidade_votos.index(lista_por_ordem[1])]
    print("Haverá segundo turno entre: " + primeiro + " e " + segundo + ".")
    print(primeiro)
    print(segundo)

total_votos = sum(quantidade_votos)
print("A eleição se encerra com um total de", total_votos, "votos, sendo", total_votos_validos, "votos válidos.")