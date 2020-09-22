# Entrada e impressao de dados
a = int(input("Digite um valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))

# input sempre retorna uma string, por isso convertemos para int

print ("Valor a: %s " %"doze")
print ("Valor b: %d" %b) # Qual valor deve ser marcado em %d
print ("Soma: %d" %(a+b))
print ("Float formatado: %.2f" %2.4214543244)
print ("Teste %s, %d, %.3f" %("marcadores", a, 12.5312412))

'''
  ---- Marcadores
  %d => decimal
  %f => float
  %s => string

  Quando necessario mais de um valor, precisa passar uma lista
  %("string", 12, 12.42112) => respectivamente no print, %s %d %.3f
'''
