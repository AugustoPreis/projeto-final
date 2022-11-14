from src.banco import banco

nomeArquivo = 'manutencao'

def proximoId():
	itens = banco.selecionar(nomeArquivo)

	return len(itens) + 1

def salvar(dados):
	banco.salvar(dados, nomeArquivo)