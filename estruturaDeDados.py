# list e mutavel
lista = ['a','b','c',1,2]
print(lista, lista[2])
lista[2] = 'ce'
lista.pop()
lista.append('novo item')
lista.remove('b') # remove a primeira ocorrencia
lista.insert(1, 'be')
lista.insert(0, 'inicio')
lista.reverse()
lista.sort(reverse=True)
# para cada item na lista
for item in lista: print(item)


# imutavel
# tuples => funcoes com mais de um valor
tupla = (11,22,33)
tupla2 = 44,55,'string'

# set
# lista, mas nao aceita repeticoes
s = set()
s.add(1)
s.add(12)
s.add(14)
s.add(14)
s.remove(12)
print(s)


# dictionary
# armazena dados atraves de chaves e valores
dictionary = {}

dictionary['nome'] = 'Miro'
dictionary['idade'] = 20
dictionary['telefone'] = '1199998888'
dictionary.pop('telefone')
print(dictionary.values())
