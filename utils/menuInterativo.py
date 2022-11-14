from pick import pick


def menuInterativo(parametros):
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

	return { 'opcao': opcao, 'index': index }