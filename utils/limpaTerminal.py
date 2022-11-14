import os


def limpaTerminal():
	comando = 'clear'
	
	if os.name in ('nt', 'dos'): 
		comando = 'cls'
	
	executaComando(comando)

def executaComando(comando):
	try:
		os.system(comando)
	except Exception as Erro:
		print('Erro ao executar "' + comando + '": ' + Erro)