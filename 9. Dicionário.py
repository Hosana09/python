###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Ballon d'Or
###################################################

# Leitura de dados
quant_jorn = int(input())
nota_jog = quant_jorn * 5
ranking = {}

# Processamento
for n in range(0, nota_jog):
    nome = input()
    valor = 6
    if not nome in ranking:
        ranking[nome] = valor
        
    else:
        ranking[nome] = valor + valor
        

# Impressão da saída
