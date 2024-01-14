###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - BikeMax
###################################################

print("Vamos descobrir qual é a bicicleta perfeita para você!")
# Leitura de dados
sexo = input("Qual o seu sexo? Digite M para masculino e F para feminino: ")
peso = float(input("Qual o seu peso? "))
#Arredondar os valores
altura = int(input("Qual a sua altura? Digite em cm: "))
#Escrever altura em cm

# Seleção do modelo recomendado
if (sexo == "M" or "m"):
    if (peso <= 70 and 150 >= altura <= 165):
        print("LX-39")
    elif (70 < peso <= 100 and 150 <= altura <= 165):
        print("LX-40")
    elif (peso <= 80 and 165 < altura <= 190):
        print("BW-02")
    elif (80 < peso <= 100 and 165 < altura <= 190):
        print("MM-107")
    elif (50 >= peso <= 100 and altura > 190):
        print("MM-107")
    else:
        print("CX-102")
elif (sexo == "F" or "f"):
    if (peso != 0 and altura <=140):
        print("LX-38")
    elif (peso <= 90 and 140 < altura <= 155):
        print("BW-03")
    elif (peso <= 70 and 155 < altura <= 170):
        print("BW-03")
    elif (peso > 90 and 140 < altura <= 155):
        print("CX-101")
    elif (peso > 70 and 155 < altura <= 170):
        print("CX-101")
    elif (peso <= 90 and altura > 170):
        print("BW-02")
    elif (peso > 90 and altura > 170):
        print("CX-102")
