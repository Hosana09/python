###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - BikeMax
###################################################

print("Vamos descobrir qual é a bicicleta perfeita para você!")
# Leitura de dados
sexo = input("Qual o seu sexo? Digite M para masculino e F para feminino: ")
if (sexo == "m" or sexo =="M" or sexo == "f" or sexo == "F"):
    peso = float(input("Qual o seu peso? ")) 
    altura = int(input("Qual a sua altura? Digite em cm: ")) #Escrever altura em cm

    # Seleção do modelo recomendado
    if (sexo == "M" or sexo =="m"):
        if (peso <= 70 and 150 >= altura <= 165):
            print("A bicicleta perfeita para você é a LX-39!")
        elif (70 < peso <= 100 and 150 <= altura <= 165):
            print("A bicicleta perfeita para você é a LX-40!")
        elif (peso <= 80 and 165 < altura <= 190):
            print("A bicicleta perfeita para você é a BW-02!")
        elif (80 < peso <= 100 and 165 < altura <= 190):
            print("A bicicleta perfeita para você é a MM-107!")
        elif (50 >= peso <= 100 and altura > 190):
            print("A bicicleta perfeita para você é a MM-107!")
        else:
            print("A bicicleta perfeita para você é a CX-102!")
    elif (sexo == "F" or sexo =="f"):
        if (peso != 0 and altura <=140):
            print("A bicicleta perfeita para você é a LX-38!")
        elif (peso <= 90 and 140 < altura <= 155):
            print("A bicicleta perfeita para você é a BW-03!")
        elif (peso <= 70 and 155 < altura <= 170):
            print("A bicicleta perfeita para você é a BW-03!")
        elif (peso > 90 and 140 < altura <= 155):
            print("A bicicleta perfeita para você é a CX-101!")
        elif (peso > 70 and 155 < altura <= 170):
            print("A bicicleta perfeita para você é a CX-101!")
        elif (peso <= 90 and altura > 170):
            print("A bicicleta perfeita para você é a BW-02!")
        elif (peso > 90 and altura > 170):
            print("A bicicleta perfeita para você é a CX-102!")
else:
    print("Você precisa digitar M ou F para dizer qual é o seu sexo...")