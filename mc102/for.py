###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Batalha na Ponte de Piltover
###################################################

# Leitura da vida de Jinx e Ekko
print("Bem vindo ao jogo Batalha na Ponte de Piltover!")
hp_jinx = int(input("Digite a quantidade de pontos de vida da Jinx: ")) #pontos de vida Jinx
hp_ekko = int(input("Digite a quantidade de pontos de vida do Ekko: ")) #pontos de vida Ekko

# Leitura dos ataques da Jinx
quantidade_ataque_jinx = int(input("Digite a quantidade de ataques da Jinx: ")) #quantidade de ataques Jinx

for n in range (0, quantidade_ataque_jinx):
    valor_ataque_jinx = int(input("Qual o valor desse ataque da Jinx? "))
    if (hp_jinx < hp_ekko):
        valor_ataque_jinx = valor_ataque_jinx // 2
        hp_ekko = hp_ekko - valor_ataque_jinx
    elif (hp_jinx >= hp_ekko):
        hp_ekko = hp_ekko - valor_ataque_jinx
    elif hp_jinx <= 0:
        break

# Leitura dos ataques do Ekko
quantidade_ataque_ekko = int(input("Digite a quantidade de ataques do Ekko: "))
            
for i in range (0, quantidade_ataque_ekko):
    valor_ataque_ekko = int(input("Qual o valor desse ataque do Ekko? "))
    if (hp_ekko <= 0):
        break
    if (hp_ekko < hp_jinx):
        valor_ataque_ekko = valor_ataque_ekko // 2
        hp_jinx = hp_jinx - valor_ataque_ekko
    elif (hp_ekko >= hp_jinx):
        hp_jinx = hp_jinx - valor_ataque_ekko

# Impressão das informações de saída
if (hp_ekko > 0 and hp_jinx > 0):
    print("Vida da Jinx:", hp_jinx)
    print("Vida do Ekko:", hp_ekko)
elif (hp_ekko == 0 and hp_jinx == 0):
    print("Vida da Jinx:", 0)
    print("Vida do Ekko:", 0)
elif (hp_ekko <= 0):
    print("Vida da Jinx:", hp_jinx)
    print("Vida do Ekko:", 0)
elif (hp_jinx <= 0):
    print("Vida da Jinx:", 0)
    print("Vida do Ekko:", hp_ekko)

if (hp_jinx > hp_ekko):
    print("Jinx foi a vencedora da batalha!")
elif (hp_ekko > hp_jinx):
    print("Ekko foi o vencedor da batalha!")
else:
    print("A batalha terminou empatada...")
