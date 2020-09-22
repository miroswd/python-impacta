# Classe
# interpretar como uma receita
  # atributos => ingredientes
  # metodos => modo de fazer

# classe Pessoa
  # atributos => nome, idade e sexo
  # metodos => andar, comer e dormir

''' # Criando um Objeto
p = Pessoa() # Declara variavel referenciando a classe Pessoa
p.nome = 'Miro'
p.idade = 20
p.sexo = 'M'
'''

# ---Objetos
  # variavel que armazena um valor do tipo de uma classe

# ---Heranca
  # herda atributos e metodos de outra classe
  # criando um objeto professor
  ''' Professor
  lecionar()
  '''
  # herdou as caracteristicas do objeto Pessoa
  # com uma nova funcionalidade
  # pessoa e o pai da classe professor

# --- Polimorfismo
  # significa 'muitas formas'
  ''' Professor
  lecionar()
  dormir()
  '''
  ''' Aluno
  lecionar()
  dormir()
  '''

  # o dormir invocado, sera do professor ou do aluno, pois dormem de forma diferente

# object => objeto que sera pai da classe, se nao herdar usa o object
class Pessoa(object):

