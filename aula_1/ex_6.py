def receber_inteiro(mensagem):
	valor = input(mensagem)
	if valor.isnumeric():
		return valor
	print ('numero inválido')
	exit()



def receber_inteiro_2(mensagem):
	valor = input(mensagem)
	while not valor.isnumeric():
		valor = input(mensagem)
	return int (valor)	

usuario = {
 'nome': input('Digite seu nome: '),
 'idade':receber_inteiro_2('Digite sua idade'),
 'peso':receber_inteiro_2('Digite seu peso')
}


print ('numero inválido')
exit()