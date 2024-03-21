###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Detector de Palíndromos
###################################################

# DICA: use os métodos lower, replace, split e index

# Leitura de dados
print("Você sabia? Um palíndromo é uma palavra ou frase que pode ser lida no seu sentido normal, da esquerda para a direita, bem como no sentido contrário, da direita para a esquerda, sem que haja mudança nas palavras que a formam e no seu significado.")
n_linhas = int(input("Digite quantos textos você gostaria de verificar se possuem palíndromos: "))

# Leitura das linhas do texto e tratamento
texto_completo = []

for n in range(0, n_linhas):
    texto = input("Digite o texto: ")
    texto = texto.lower()
    texto = texto.replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "")
    texto = texto.split()
    texto_completo.extend(texto)

# Processamento
palindromos = []

for cada in texto_completo:
    if cada == cada[::-1] and cada not in palindromos:
        palindromos.append(cada)
        print("A palavra", cada, "é um palíndromo e ela aparece", texto_completo.count(cada), "vez(es) no texto.")
