import src.manutencao.manutencao as manutencao
from src.menu.menu import menu
from src.relatorios.menu import menu as menuRelatorios
from utils.limpaTerminal import limpaTerminal
from utils.menuInterativo import menuInterativo

while(True):
	opcao = menu()

	if(opcao == 0):
		manutencao.cadastro()
	elif (opcao == 1):
		manutencao.alteracao()
	elif (opcao == 2):
		manutencao.realizar()
	elif (opcao == 3):
		manutencao.finalizar()
	elif (opcao == 4):
		menuRelatorios()
	else:
		break