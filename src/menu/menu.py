from utils.menuInterativo import menuInterativo


def menu():
	opcoesMenu = {
		'titulo': 'Selecione a opção desejada:',
		'indicador': '>',
		'opcoes': [
			'Cadastrar Manutenção',
			'Alterar Manutenção',
			'Realizar Manutenção',
			'Finalizar Manutenção',
			'Relatórios',
			'Sair',
		],
	}

	dados = menuInterativo(opcoesMenu)

	return dados['index']