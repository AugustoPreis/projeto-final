from tabulate import tabulate


def imprimir(dados):
  valores = [
		[
			'ID',
			'Nome Titular',
			'CPF',
			'Tipo Veículo',
			'Valor',
			'Entrada',
			'Saída',
		]
	]

  for item in dados:
    valores.append([
			item['id'],
			item['nomeTitular'],
			item['cpf'],
			item['tipoVeiculo'],
			item['valorOrcamento'],
			item['dataEntrada'],
			item['dataSaida'],
		])

  print(tabulate(valores, headers='firstrow'))