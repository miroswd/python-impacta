class Carro(object):
  def __init__(self, caminho):
    # metodo constructor
    # todo metodo q comeca com __ e termina com __
    # sao metodos internos, nao invocamos diretamente
    # o python q faz isso
    self.caminho = caminho


  def andar(self):
    # self.caminho = 'Rua'
    print("Andando pela %s" %self.caminho)

# >>> python from carro import Carro
# toda vez que mudar o codigo, e estiver usando o terminal
# necessita importar o modulo de novo

# -- No terminal
# python
# from carro import Carro
# c = Carro() # instanciando a class
# c.andar() # executa o metodo andar
# c.caminho = "estrada" # altera o valor da variavel caminho
# mas ao executar c.andar(), retorna o valor antigo, ja que
# a variavel esta sendo definida dentro do metodo
# para isso, devemos criar a variavel, assim q a classe for criada
# no metodo constructor

# --- Conceitos de Heranca
# informamos a classe pai entre parenteses, se o pai foi comprar
# cigarro, a classe nao tem pai, usar object == class SemPai(object)
class Fusca(Carro):
  # como a classe pai recebe um paramentro no constructor
  # e necessario usar os mesmos parametros
  def __init__(self,caminho):
    self.caminho = caminho

  # python
  # from carro import Fusca
  # f = Fusca("Rua")
  # f.andar() # mesmo o metodo nao estando incluso
  # na classe Filha, ele conse executar o metodo da classe pai

  # -- se precisa, q a classe filha chame um metodo da classe pai
  # usamos a funcao super

  def correr(self):
    self.caminho = "pista" # alteramos a variavel caminho
    super(Fusca, self).andar() # invocamos o metodo andar da classe pai, atraves da super
# -- Polimorfismo // um objeto e filho de outro, mas altera
# seu comportamento inicial
class Ferrari(Carro):
  def __init__(self,caminho):
    self.caminho = caminho

  # sobrescrevendo o metodo andar da classe pai
  # pois a ferrari anda diferente de um carro
  def andar(self):
    print("Correndo muito pela %s" %self.caminho)
