from utils.menuInterativo import menuInterativo
from src.menu.opcoes import opcoes

def menu():
	opcoesMenu = {
		'opcoes': opcoes,
		'titulo': 'Selecione a opção desejada:',
		'indicador': '>',
	}

	dados = menuInterativo(opcoesMenu)

	#Retorna o index da opcao na variavel "opcoes"
	return dados['index']