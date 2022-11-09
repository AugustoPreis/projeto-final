from utils.limpaTerminal import limpaTerminal 
from utils.menuInterativo import menuInterativo

from src.menu.menu import menu
import src.manutencao.manutencao as manutencao
from src.relatorios.menu import menu as menuRelatorios

def iniciaPrograma():
	#Limpa o terminal para iniciar o programa
	limpaTerminal()

	#Salva opção do menu selecionada pelo usuário
	#Opções estão em: src > menu > opcoes.py
	opcao = menu()

	#Chama função que realiza a ação determinada pelo usuário
	if(opcao == 0):
		manutencao.cadastroManutencao()
	elif (opcao == 1):
		manutencao.alteraManutencao()
	elif (opcao == 2):
		manutencao.realizaManutencao()
	elif (opcao == 3):
		manutencao.finalizaManutencao()
	elif (opcao == 4):
		menuRelatorios()
	elif (opcao == 5):
		print('Programa finalizado com sucesso!')
		return

	opcoesMenu = {
		'titulo': 'Deseja realizar outra ação?',
		'opcoes': ['Sim', 'Não']
	}

	opcao = menuInterativo(opcoesMenu)

	#Caso o usuário queira continuar, ele reinicia o sistema, chamando novamente a função iniciaPrograma
	if(opcao['index'] == 0):
		iniciaPrograma()

iniciaPrograma()