#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Plataforma
#####################################################

"""
Esta função recebe como parâmetro uma lista que representa o tamanho do salto 
que pode ser dado em cada ponto de uma plataforma. Além disso, uma posição inicial 
na plataforma é determinada pelo parâmetro i. O retorno esperado para a função é 
um valor booleano, com True indicando que foi possível sair da plataforma e False 
indicando que o personagem ficou preso na plataforma (loop).
"""

#lista com o tamanho do salto
plataforma = input().split(" ")
#recebe posição inicial
i = int(input())


def salto(plataforma, i):
  i = i - 1
  if i > len(plataforma) - 1 or i < 0:
    print("Saiu da plataforma")
  else:
    if plataforma[i] == 1:
      i = i + 1
      if plataforma[i] == 0:
        i = i - 2
        if plataforma[i] == 0:
          print("Loop")
        return salto(plataforma, i + 1)
    elif plataforma[i] >= 2:
      i = i + 1
      return salto(plataforma, i + 1)
    elif plataforma[i] == 0:
      return salto(plataforma, i)
