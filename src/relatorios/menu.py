import src.relatorios.relatorios as relatorios
from utils.limpaTerminal import limpaTerminal
from utils.menuInterativo import menuInterativo


def menu():
	opcoes = {
		'titulo': 'Selecione o relatório desejado',
		'indicador': '>',
		'opcoes': [
			'Todas as manutenções',
			'Manutencões com status A',
			'Manutencões com status M',
			'Manutencões com status C',
			'Manutencões com status F',
			'Sair',
		],
	}

	index = menuInterativo(opcoes)['index']

	if (index == 0):
		relatorios.todasManutencoes()
	elif (index == 1):
		relatorios.manutencoesPorStatus('A')
	elif (index == 2):
		relatorios.manutencoesPorStatus('M')
	elif (index == 3):
		relatorios.manutencoesPorStatus('C')
	elif (index == 4):
		relatorios.manutencoesPorStatus('F')
	else:
		return
	
	input('\n\nAperte ENTER para continuar')

	limpaTerminal()