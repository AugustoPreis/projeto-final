from datetime import datetime

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


def buscaPorStatus(status):
  dados = banco.selecionar(nomeArquivo)

  return list(filter(lambda item: item['status'] == status, dados))

def realizar(index):
  itens = banco.selecionar(nomeArquivo)

  itens[index]['status'] = 'M'

  banco.atualizar(itens, nomeArquivo)

def finalizar(index):
  itens = banco.selecionar(nomeArquivo)
  
  itens[index]['dataSaida'] = datetime.now().strftime('%d/%m/%y %H:%M')
  itens[index]['status'] = 'F'

  banco.atualizar(itens, nomeArquivo)

def alterar(item):
  dados = banco.selecionar(nomeArquivo)
  index = int(item['id']) - 1

  dados[index] = item

  banco.atualizar(dados, nomeArquivo)