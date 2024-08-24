print(3+5)
print("Olá, Mundo!")

x = 10
print(x)

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
while a < b:
    print(a)
    a += 1
print(a)
print("Fim do programa.")

# Isso é um comentário!

def soma(a, b):
 """
 Função para somar dois números.

 Args:
 a (float): O primeiro número.
 b (float): O segundo número.

 Returns:
 float: A soma dos dois números.
 """
 return a + b
print(soma(2,3))

import math
import random as rd
# imprime o valor de PI
print(math.pi)
# imprime o valor de RAIZ de 2
print(math.sqrt(2))
# gera um número aleatório entre 0 e 10
print(rd.randint(0,10))

idade = 25
altura = 1.75
letra = 'A'
type(idade)
type(altura)
type(letra)

idade = 25
altura = 1.76
print(f'A altura é {altura} e a idade é {idade}')

x = 10
y = 20
z = x * y
print("z = ",z)
z = y/10
print("z = ",z)
print("x+y = ",x+y)

x = 5
y = 3
print("Expressão 1: ",x > 4)
print("Expressão 2: ",x == 4)
print("Expressão 3: ",x != y)
print("Expressão 4: ",x != y+2)

r = (x > 2) and (y < x)
print("Resultado: ",r)
r = (x%2==0) and (y > 0)
print("Resultado: ",r)
r = (x > 2) or (y > x)
print("Resultado: ",r)
r = (x%2==0) or (y < 0)
print("Resultado: ",r)
r = not(x > 2)
print("Resultado: ",r)
r = not(x > 7) and (x > y)
print("Resultado: ",r)
