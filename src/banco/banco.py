def selecionar(nome):
	arquivo = open(rf'./src/banco/{nome}.txt', 'r')

	itens = arquivo.readlines()

	arquivo.close()

	return itens

def salvar(dados, nome):
	arquivo = open(rf'./src/banco/{nome}.txt', 'r+')

	itens = arquivo.readlines()

	item = str(dados)

	if(len(itens) > 0):
		item = '\n' + item

	arquivo.writelines(item)

	arquivo.close()