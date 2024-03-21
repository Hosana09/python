# Classes são a abstração do mundo real em código
# Um objeto é a instância de uma classe

class Restaurante: 
    nome = ""
    categoria = ""
    ativo = False

restaurante_praça = Restaurante() #para criar um objeto utiliza o nome da classe seguida do de ()
restaurante_praça.nome = "Praça" #utiliza o ponto para acessar o objeto
restaurante_praça.categoria = "Italiana"
print(restaurante_praça) #visualiza o endereço de memória
print(dir(restaurante_praça)) #visualiza os métodos da classe
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ativo', 'categoria', 'nome']
print(vars(restaurante_praça)) #visualiza um dicionário com os atributos e métodos
#{'nome': 'Praça', 'categoria': 'Gourmet'}
print(restaurante_praça.nome) #visualiza o valor do atributo
#Praça
print(restaurante_praça.categoria)
#Italiana
print(restaurante_praça.ativo)
#False
print(f'Atualmente, o Restaurante praça está {restaurante_praça.ativo}.')

nome_do_restaurante = restaurante_praça.nome #acessando o valor do atributo nome

if restaurante_praça.ativo:
    print("O restaurante está ativo.")
else:
    print("O restaurante está inativo.")

print(f'Nome: {restaurante_praça.nome}, Categoria: {restaurante_praça.categoria}.')

restaurante_barato = Restaurante()
restaurante_barato.nome = "Barato"
restaurante_barato.categoria = "Bar"

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"
restaurante_pizza.ativo = True
print(restaurante_pizza.categoria)

restaurantes = [restaurante_praça, restaurante_barato]
print(restaurantes)
#[<__main__.Restaurante object at 0x000001F4C498B700>, <__main__.Restaurante object at 0x000001F4C498B6D0>]

class Musica:
    nome = ""
    artista = ""
    duracao = int

musica_adele = Musica()
musica_adele.nome = "Skyfall"
musica_adele.artista = "Adele"
musica_adele.duracao = 289 #segundos