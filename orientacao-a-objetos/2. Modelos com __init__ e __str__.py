# O __init__ é um método construtor responsável por construir com modelo construtor e é sempre chamado quando criamos uma instância de um objeto e espera uma informação (por isso os parênteses)
# O self informa que que se trata daquele objeto que está sendo referenciado no momento. É a referência da instância utilizada
# O __str__ é um método para mostrar o objeto em formato de texto

class Restaurante: 
    def __init__(self, nome, categoria): 
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'


restaurante_praca = Restaurante("Praça", "Italiana")
print(restaurante_praca) #objeto na memória, mas depois de colocar o __str__ ele vai retornar o que estiver na função 
print(vars(restaurante_praca))

restaurante_pizza = Restaurante("Pizza Place", "Fast Food")
print(restaurante_pizza)
print(vars(restaurante_pizza)) #dicionário com os atributos e seus valores