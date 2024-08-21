###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Encaixe Perfeito
###################################################

# Leitura do número de partidas
print("Você já brincou de Encaixe Perfeito?")
n = int(input("Diegite o número de partidas: "))

for _ in range(n): # Leitura das peças 1 e 2
  P1 = [int(i) for i in input().split()] #monta lista com numeros tirando o espaço
  P2 = [int(i) for i in input().split()]

# Processamento das possibilidades de encaixe
qnt_encaixe = (len(P2) - len(P1)) + 1
altuma_max = 0
max_p1 = max(P1)
max_p2 = max(P2)
altura_max = max_p2 + max_p1

for n in qnt_encaixe:
  for h in P2:
    soma_altura = P2 + P1
  
  forma_encaixe = "Normal"

if (numero_espacos != 0):
  P1 = P1.reverse()
  forma_encaixe = "Invertida"

  # Impressão da saída esperada para cada partida
  print("Pontuacao:", P)
  print("Encaixe Perfeito!")
  print("Posicao de Encaixe:", forma_encaixe)
  print("Peca 1:", S)
