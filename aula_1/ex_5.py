opcao = None
while opcao != '3':
	print('1- Cadastrar novo usuario')
	print('2 - Ver usuários cadastrados')
	print('3 - Sair')
	opcao = input( 'Seleciona uma das opções: ')
print('Fim do programa')

numero = ''
while not numero.isnumeric():
	numero = input ('Digite um numero :'
		)
	print (numero)