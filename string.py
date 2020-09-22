# sequencia de caracteres, entre aspas

print("String", 'outro tipo')
print('''
multiplas
linhas
''')

print('fa t iando'[-3:])
print('fatiando de 2 em 2'[0::2])


# Verificar se a paavra e um Palindromo

def palindromo(palavra):
  if (palavra == palavra[::-1]):
    print ('sim')
  else:
    print('nem')

palindromo('po')
