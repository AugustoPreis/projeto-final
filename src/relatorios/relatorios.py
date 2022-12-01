import src.banco.banco as banco
import src.manutencao.repositorio as repositorio
from utils.tabelaRelatorio import imprimir

nomeArquivo = 'manutencao'

def todasManutencoes():
	dados = banco.selecionar(nomeArquivo)

	if (len(dados) == 0):
		return print('\nNenhuma manutenção encontrada')

	imprimir(dados)

def manutencoesPorStatus(status):
	dados = banco.selecionar(nomeArquivo)
	dados = list(filter(lambda item: item['status'] == status, dados))

	if (len(dados) == 0):
		return print('\nNenhuma manutenção encontrada')

	imprimir(dados)

def manutencoesPorPessoa():
	cpf = input('Digite o cpf: ')
	dados = repositorio.buscaPorCpf(cpf)

	if (len(dados) == 0):
		return print('\nNenhuma manutenção encontrada')

	imprimir(dados)

def totalRecebido():
	dados = repositorio.buscaPorStatus('F')
	total = 0

	if (len(dados) == 0):
		return print('\nNenhuma manutenção encontrada')

	for item in dados:
		try:
			total += float(item['valorOrcamento'])
		except:
			pass

	imprimir(dados)

	print(f'\nValor total: {str(total)}')
	return