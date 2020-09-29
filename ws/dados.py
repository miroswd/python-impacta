import requests
# import json
import csv
import json, ast
import string


data = requests.get("https://servicos.jfrn.jus.br/faleconoscoapi")
# j = json.loads(d)
toCSV = data.text.encode('utf-8')
# print(toCSV)



keys = data.json()[0].keys()
# values = data.json()[0].values()
key = ast.literal_eval(json.dumps(keys)) # removendo o u'key'
# value = ast.literal_eval(json.dumps(values)) # removendo o u'key'
values = json.dumps(data.json()[0].values(), ensure_ascii=False).encode('utf8')
# keys = json.dumps(data.json()[0].keys(), ensure_ascii=False).encode('utf8')
k = data.json()[0].keys()
v = data.json()[0].values()
kx = [str(x) for x in k]
opa = data.json()
dataJson = json.dumps(opa[2], ensure_ascii=False).encode('utf8')
# po = json.load(opa)
# print(dataJson)
array = []
for i in range(0,2):
  # print(data.json()[i])
  array.append(data.json()[i])


# teste = [{'resposta':'miro'},{'dataMensagem':'miroleto'},{'id':'12'},{'dataResposta':'respo'},{"mensagem":"dataRespostaas"}]
# with open('faleConosco.txt', 'w') as output_file:
  # print(output_file)
  arquivo = ('teste.txt','w')
  arquivo.write(data)
  arquivo.close()
  # fc = csv.DictWriter(output_file, teste.json().keys)
  # fc.writeheader()
  # fc.writerows(data)

