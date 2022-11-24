from src.banco import banco

nomeArquivo = 'manutencao'

def proximoId():
	itens = banco.selecionar(nomeArquivo)

	return len(itens) + 1

def salvar(dados):
	banco.salvar(dados, nomeArquivo)

def buscaPorCpf(cpf):
  dados = banco.selecionar(nomeArquivo)

  return list(filter(lambda item: item['cpf'] == cpf, dados))

def realizar(index):
  itens = banco.selecionar(nomeArquivo)

  itens[index]['status'] = 'M'

  banco.atualizar(itens, nomeArquivo)