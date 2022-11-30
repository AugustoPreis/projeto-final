from src.manutencao import repositorio
from utils.menuInterativo import menuInterativo


def cadastro():
	dados = solicitaDadosCadastro()

	if (dados['nomeTitular'] == None):
		return print('Nome inválido, cadastro cancelado!')

	if (dados['cpf'] == None):
		return print('CPF inválido, cadastro cancelado!')

	if (dados['detalhesOrcamento'] == None):
		return print('Detalhe inválido, cadastro cancelado!')

	if (dados['valorOrcamento'] == None):
		return print('Valor inválido, cadastro cancelado!')

	if (dados['dataEntrada'] == None):
		return print('Data de entrada inválida, cadastro cancelado!')

	repositorio.salvar(dados)

def solicitaDadosCadastro():
	opcoesMenuTipoVeiculo = {
		'titulo': 'Tipo do veículo',
		'opcoes': [
			'Carro',
			'Moto',
			'Outros',
		],
	}

	opcoesKeys = ['C', 'M', 'O']

	id = repositorio.proximoId()

	nomeTitular = input('Nome do titular: ')

	cpf = input('CPF do titular: ')

	tipoVeiculoObj = menuInterativo(opcoesMenuTipoVeiculo)

	tipoVeiculo = opcoesKeys[tipoVeiculoObj['index']]

	print('Tipo do veículo: ' + tipoVeiculoObj['opcao'])

	detalhesOrcamento = input('Detalhes do orçamento: ')

	valorOrcamento = input('Valor do orçamento: ')

	descricaoServico = input('Descrição do serviço: ')

	dataEntrada = input('Data de entrada (dia/mês/ano): ')

	dataSaida = None

	status = 'A'

	return {
		'id': id,
		'nomeTitular': nomeTitular,
		'cpf': cpf,
		'tipoVeiculo': tipoVeiculo,
		'detalhesOrcamento': detalhesOrcamento,
		'valorOrcamento': valorOrcamento,
		'descricaoServico': descricaoServico,
		'dataEntrada': dataEntrada,
		'dataSaida': dataSaida,
		'status': status,
	}

def alteracao():
  global id
  cpf = input('Digite o CPF: ')
  dados = repositorio.buscaPorCpf(cpf)

  if (len(dados) == 0):
    return print('Nenhuma manutenção encontrada')
  elif (len(dados) == 1):
    id = dados[0]['id']
    item = solicitaDadosAlteracao(dados[0])

    repositorio.alterar(item)
  else:
    opcoesMenu = {
      'titulo': 'Selecione a manutenção desejada:',
      'indicador': '>',
      'opcoes': list(map(lambda item: (str(item['id']) + ' - ' + item['dataEntrada']), dados)),
    }

    item = menuInterativo(opcoesMenu)['index']

    id = dados[item]['id']

    dados[item] = solicitaDadosAlteracao(dados[item])

    repositorio.alterar(dados[item])

  print('Manutenção ' + str(id) + ' finalizada!')
  input('\n\nAperte ENTER para continuar')

def solicitaDadosAlteracao(dados):
  dados['detalhesOrcamento'] = input('Digite os detalhes do orcamento: ')
  dados['valorOrcamento'] = input('Digite o valor do orçamento: ')
  dados['descricaoServico'] = input('Digite a descrição do serviço: ')
  dados['status'] = input('Digite o status da manutencao: ')

  return dados

def finalizar():
  global id
  cpf = input('Digite o CPF: ')
  dados = repositorio.buscaPorCpf(cpf)
  dados = list(filter(lambda item: item['status'] == 'M', dados))

  if (len(dados) == 0):
    return print('Nenhuma manutenção encontrada')
  elif (len(dados) == 1):
    id = dados[0]['id']

    repositorio.finalizar(id - 1)
  else:
    opcoesMenu = {
      'titulo': 'Selecione a manutenção desejada:',
      'indicador': '>',
      'opcoes': list(map(lambda item: (str(item['id']) + ' - ' + item['dataEntrada']), dados)),
    }

    item = menuInterativo(opcoesMenu)['index']

    id = dados[item]['id']

    repositorio.finalizar(id - 1)

  print('Manutenção ' + str(id) + ' finalizada!')
  input('\n\nAperte ENTER para continuar')

def realizar():
  global id
  cpf = input('Digite o CPF: ')
  dados = repositorio.buscaPorCpf(cpf)
  dados = list(filter(lambda item: item['status'] != 'M', dados))

  if (len(dados) == 0):
    return print('Nenhuma manutenção encontrada')
  elif (len(dados) == 1):
    id = dados[0]['id']

    repositorio.realizar(id - 1)
  else:
    opcoesMenu = {
      'titulo': 'Selecione a manutenção desejada:',
      'indicador': '>',
      'opcoes': list(map(lambda item: (str(item['id']) + ' - ' + item['dataEntrada']), dados)),
    }

    item = menuInterativo(opcoesMenu)['index']

    id = dados[item]['id']

    repositorio.realizar(id - 1)

  print('Manutenção ' + str(id) + ' iniciada!')
  input('\n\nAperte ENTER para continuar')