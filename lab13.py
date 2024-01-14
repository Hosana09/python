#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - 6174
#####################################################

# Leitura do número N
#N é o número normal
N = input()

# Repetição do processo para geração de f(N) até obtermos o número 6174
def kaprekar(N):
    print(N)
    while N != "6174":
        C = int(''.join(sorted(N)))
        D = int(''.join(sorted(N, reverse=True)))
        N = str(D - C)
        print(N)

#chamar a função
kaprekar(N)
