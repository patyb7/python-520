banco_de_dados =[]
def cadastrar_usuario(usuario):
	global banco_de_dados
	banco_de_dados.append(usuario)
def consultor_usar (email):
	for usuario in banco_de_dados:
		if usuario['email']	== email:
			return usuario
	return None
def receber_input(mensagem, bloquear=True)
	if not bloquear:
		valor = input(mensagem)
		if not valor.isnumeric():
			exit()
		return int(valor)
	else:
		valor =''
		while not valor.isnumeric():
			valor = input(mensagem)
		return int(valor)
mensagem = 'duasidhuas'
receber_input(mensagem,bloquear=True)
receber_input(mensagem)