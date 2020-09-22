# Read
# modo leitura ja esta embutido, nao precisa carregar modulo

# o arquivo deve permanecer no mesmo diretorio do arquivo py
def readFile(file):
  arquivo = open(file,'r') # funcao open('nome','modo de manipulacao (r > read, w > write, a > apend, incluir depois do conteudo do arquivo, r+ > read e write)')

  for linha in arquivo:
    print(linha)
  arquivo.close()

# no windows tem q passar o b, rb, wb, ab, r+b, pois o windows difere arquivos txt de binario


def saveFile(file, newText):
  arquivo = open(file,'w')
  arquivo.write(newText)
  arquivo.close()
# Quando usar arquivos externos, sempre fechar o processo
# para evitar um bloqueio de acesso
saveFile('bomDia.txt', 'Hello World!')
readFile('bomDia.txt')
