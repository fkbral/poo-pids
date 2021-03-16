class Jogador:
  def __init__(self, name, age, points = 0):
    self.nome = name
    self.idade = age
    self.pontuacao = points

  def imprimeDados(self):
    print('Nome do jogador:', self.nome)
    print('Idade do jogador:', self.idade)
    print('Pontuacao do jogador:', self.pontuacao)

class Animal:
  def __init__(self, species, region):
    self.especie = species
    self.regiao = region


  # def atualizaNome(self)

jogador1 = Jogador('Felipe', 29)
jogador2 = Jogador('Maria', 35, 90)
# novo_jogador = Jogador()

Jogador.imprimeDados(jogador1)
jogador1.imprimeDados()
jogador2.imprimeDados()

# nome_jogador_1 = "Felipe"
# idade_jogador_1 = 29
# pontuacao_jogador_1 = 0

