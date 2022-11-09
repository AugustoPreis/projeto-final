from pick import pick, __all__

def menuInterativo(parametros):
	#Cria menu interativo com os dados informados na chamada da função
	opcoes = parametros
	itens = [
		'indexPadrao',
		'indicador',
		'minimo',
		'multi',
		'opcoes',
		'titulo',
		'mapeador',
	]

	#Caso um parâmetro não seja informado, ele seta para "None" por padrão
	for item in itens:
		if(item not in opcoes):
			opcoes[item] = None

	opcao, index = pick(
		default_index = opcoes['indexPadrao'] or 0,
		indicator = opcoes['indicador'] or '>',
		min_selection_count = opcoes['minimo'],
		multiselect = opcoes['multi'],
		options = opcoes['opcoes'] or [],
		title = opcoes['titulo'] or 'Selecione uma opção',
	)

	#Retorna um dicionário com a opção selecionada, tal como seu index no array "opcoes"
	return { 'opcao': opcao, 'index': index }