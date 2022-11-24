import json


def selecionar(nome):
	arquivo = open(rf'./src/banco/{nome}.txt', 'r')
	itens = arquivo.readlines()
	arquivo.close()
	
	return list(map(lambda item: json.loads(item), itens))

def salvar(dados, nome):
	arquivo = open(rf'./src/banco/{nome}.txt', 'r+')
	item = str(json.dumps(dados))

	if(len(arquivo.readlines()) > 0):
		item = '\n' + item

	arquivo.writelines(item)

	arquivo.close()

def atualizar(dados, nome):
	arquivo = open(rf'./src/banco/{nome}.txt', 'w')

	for i in range(len(dados)):
		dados[i] = json.dumps(dados[i])

		if (i != 0):
			dados[i] = '\n' + dados[i]

	arquivo.writelines(dados)
	arquivo.close()