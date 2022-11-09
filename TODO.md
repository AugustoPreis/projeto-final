Cadastro de Manutenção

	ID

	Nome do Titular (Obrigatório)

	CPF (Obrigatório)

	Tipo do Veículo (C – Carro, M – Moto, O – Outros)

	Detalhe: ex: Marca, Modelo, Cor (Obrigatório)

	Valor do orçamento (Obrigatório)

	Descrição do serviço

	Data da Entrada (Obrigatório)

	Data da Saída (no momento do cadastro essa data deve ficar em branco)

	Status
		(
			A – Aguardando para manutenção (Colocar este no momento do cadastro),
			M – Em manutenção,
			C - Cancelado,
			F - Finalizado
		)

	Caso algum campo obrigatório não seja preenchido, o sistema voltará automaticamente para o início do cadastro

	Ao realizar o cadastro, o sistema deverá mostrar a seguinte mensagem: ‘Cadastro Realizado com sucesso!’

Realizar manutenção:
	Nessa tela o usuário terá a opção de dar entrada no processo de manutenção.
	Para isso o usuário deverá realizar a busca de manutenção pelo CPF.
	Caso exista mais de uma manutenção no CPF da pessoa, o usuário deverá escolher qual manutenção ele quer dar entrada.

	O processo de entrada na manutenção é automático, apenas alterar o status para M.
	
	O sistema deverá apresentar a mensagem de realização: ‘A manutenção "8521" foi iniciada!’

Finalizar manutenção:
	Nessa tela o usuário terá a opção de finalizar um processo de manutenção.
	Para isso o usuário deverá realizar a busca de manutenção pelo CPF.
	Deve ser listado apenas as manutenções com status M – Em manutenção.
	Caso exista mais de uma manutenção no CPF da pessoa, o usuário deverá escolher qual manutenção ele quer finalizar.

	O processo de entrada na manutenção é automático, apenas alterar o status para M, e adicionar data de saída.

	O sistema deverá apresentar a mensagem de realização, ex: ‘Manutenção 8521 finalizada com sucesso! Tempo decorrido: 20 horas’.

Alteração de manutenção
	Para isso o usuário deverá realizar a busca de manutenção pelo CPF.
	Caso exista mais de uma manutenção no CPF da pessoa, o usuário deverá escolher qual manutenção ele quer alterar.

	O sistema deverá permitir a alteração dos seguintes campos:
		Detalhe;
		Valor do orçamento;
		Descrição do serviço;
		Status;

	Ao inserir os novos dados sobre a manutenção, o sistema deverá apresentar uma mensagem de confirmação de alteração.

Relatório de Reservas

o Todas os relatórios devem conter um cabeçalho e ser apresentado de forma tabular.

Opções de impressão:

1 - Todas as manutenções.
2 - Manutenções com status A.
3 - Manutenções com status M.
4 - Manutenções com status C.
5 - Manutenções com status F.
5 - Total recebido (somar valor das manutenções finalizadas)
6 – Manutenções por pessoa (Pesquisa por CPF)