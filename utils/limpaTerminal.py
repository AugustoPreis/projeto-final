import os

def limpaTerminal():
	#Comando para limpar terminal em LINUX
	comando = 'clear'
	
	#Caso o sistema operacional for WINDOWS, troca comando para "cls"
	if os.name in ('nt', 'dos'): 
		comando = 'cls'
	
	executaComando(comando)

def executaComando(comando):
	try:
		os.system(comando)
	except Exception as Erro:
		print('Erro ao executar "' + comando + '": ' + Erro)