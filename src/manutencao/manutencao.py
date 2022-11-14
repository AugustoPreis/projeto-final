from src.banco import banco
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
	return

def finalizar():
	return

def realizar():
	return