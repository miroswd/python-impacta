import requests
import json, ast # para interpretar json
from enderecos import Endereco


cep = input("Digite o cep: ")

r = requests.get("https://viacep.com.br/ws/%s/json" %cep)
d = requests.get("https://servicos.jfrn.jus.br/faleconoscoapi")
print(d.text["dataMensagem"])

if (r.status_code == requests.codes.ok):
  j = json.loads(r.text)
  # print(j.encode('ascii'))
  endereco = Endereco()
  endereco.cep = j[u'cep']
  endereco.logradouro = j[u'logradouro']
  endereco.complemento = j[u'complemento']
  endereco.bairro = j[u'bairro']
  endereco.localidade = j[u'localidade']
  endereco.uf = j[u'uf']
  endereco.ibge = j[u'ibge']
  endereco.gia = j[u'gia']
  endereco.salvar()
else:
  print("CEP nao encontrado")
# "04685001"
