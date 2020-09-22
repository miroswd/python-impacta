# recebe params ou envia um retorno
# function serve para manter o codigo limpo, evitando
# repetir trechos de codigo

def sum(a,b):
  return a + b

def sub(a,b):
  print (a-b)
soma = sum(1,6)

sub(2,1)
print(soma)

# **kwargs => converte valores passados na function, como um dicionario

def printParams(**kwargs):
  for key, value in kwargs.items():
    print("%s:%s" %(key, value))

printParams(nome="miro", idade="20")
