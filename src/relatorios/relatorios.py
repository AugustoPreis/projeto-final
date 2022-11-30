import src.banco.banco as banco
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