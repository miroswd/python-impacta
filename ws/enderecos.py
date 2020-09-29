# ---- CRIANDO UMA CONSULTA DE CEP

import sqlite3

class Endereco(object):
  def __init__(self):
    self.cep = None
    self.logradouro = None
    self.bairro = None
    self.localidade = None
    self.uf = None
    self.ibge = None
    self.gia = None

  def cria_tabela(self):
    connection = sqlite3.connect("newenderecos.db")
    cursor = connection.cursor()

    cursor.execute('''
      CREATE TABLE IF NOT EXISTS endereco (
        cep text, ibge text, gia text
      )
    ''')

    connection.commit()

  def salvar(self):
    self.cria_tabela() # chamando a funcao cria_tabela

    connection = sqlite3.connect("newenderecos.db")
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO endereco VALUES(%s, %s, %s)
    ''' %(
      self.cep,
      self.ibge,
      # self.logradouro,
      # self.bairro,
      #  self.localidade,
      self.gia
    ))

    connection.commit()
    print('Cep: %s, encontrado e salvo com sucesso' %self.cep)
