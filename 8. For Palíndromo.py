###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Detector de Palíndromos
###################################################

# DICA: use os métodos lower, replace, split e index

# Leitura de dados

n_linhas = int(input())

# Leitura das linhas do texto e tratamento
texto_completo = []

for n in range(0, n_linhas):
    texto = input()
    texto = texto.lower()
    texto = texto.replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "")
    texto = texto.split()
    texto_completo.extend(texto)

# Processamento
palindromos = []

for cada in texto_completo:
    if cada == cada[::-1] and cada not in palindromos:
        palindromos.append(cada)
        print(cada, texto_completo.count(cada))
