import sqlite3

connection = sqlite3.connect("sqlite.db") # nome do banco
cursor = connection.cursor() # cursor => interadores que permitem navegar e manipular os registros do db
# criando cada script dentro de cada funcao, para nao executar o mesmo script 2 vezes sem querer

def criar_tabela():
  # multi paragrafo - 3 aspas
  # (nome tipo)
  sql = '''
  CREATE TABLE newalbumns(titulo text, artista text, data_lancamento text, data_publicacao text, midia text)
  '''
  # executando a variavel sql
  cursor.execute(sql)

  # toda vez que usar algum comando sql, que faca manipulacoes
  # precisa usar o comando commit, para efetivar na tabela
  connection.commit()

def gravar_album():
  sql = '''
  INSERT INTO newalbumns VALUES('Glow', 'Andy Hunter', '24/07/2012', 'Xplore Records', 'mp3')
  '''
  cursor.execute(sql)
  connection.commit()

def gravar_muitos():
  albumns = [
    ('Exodus','Andy Hunter', '09/07/2002','Sparrow Records', 'CD'),
    ('Until We Have Faces','Red', '01/02/2012','Essential Records', 'CD'),
  ]

  cursor.executemany("INSERT INTO newalbumns VALUES (?,?,?,?,?)", albumns)
  # interrogacoes, fazem o mapeamento
  # dos valores existentes dentro da tupla.
  # deve ter o mesmo numero de interrogacoes, e valores dentro da tupla

  connection.commit()

# import database
# database.gravar_muitos()

# encurtando
# import database as db
# db.gravar_muitos()

def atualiza():
  sql = '''
  UPDATE newalbumns SET artista = 'John Doe'
  WHERE artista = 'Andy Hunter'
  '''

  cursor.execute(sql)
  connection.commit()

def deleta():
  sql = '''
   DELETE FROM newalbumns WHERE artista = 'John Doe'
  '''

  cursor.execute(sql)
  connection.commit()

def listar():
  sql = '''
  SELECT rowid, * FROM newalbumns ORDER BY artista
  '''

  # rowid => identificacao do banco por cada linha
  cursor.execute(sql)

  for row in cursor.fetchall():
    # fetchall => traz do cursor toda a tabela q estamos procurando
    print(row)
