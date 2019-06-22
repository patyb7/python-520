usuario = {
	'nome': 'Paty',
	'email': 'patyb7@hotmail.com',
	'idade': input('Digite sua idade:')
}

idade = 10>50

if (idade/5)>1200:
   print ('Você é velho')
else:
   print('Você é jovem')
 	for letra in usuario['idade']:
	if letra not in '0123456789':
			print ('idade invalida')
			exit()
print('Opa tá ok')
idade = int (usuario['idade'])


#ex2: imprimir no terminal somente o nome e a idade digitados
#ex4 se o email do usuario acima nao conter um @ imprimir email
#invalido
#idade = int (usuario['idade'])
#	if(idade/5)>1200:
#		print('Você é velho')
#	else:
#		print('Você é jovem')
#idade = int(input('Digite sua idade'))


#if(idade / 5) > 1200:
#		print('Você é velho')
#else:
#	print('Você é jovem')