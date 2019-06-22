#Situação : Você é um professor e quer automatizar o cálculo 
#das médias de sua turma.
#Seu programa deve receber: 
#1 - Número de avaliações aplicadas
#2 - Para cada avaliação, digite a nota do aluno
# Ao final, calcule a média das avaliações
# e se a média for maior do que 6, imprimir
#aprovado,
#se não reprovado
 
numero_de_avaliacoes = input(MENSAGEM)
if not numero_de_avaliacoes.isnumeric():
	print('numero inválido')
	exit()
numero_de_avaliacoes

nota1 = int(input('Digite a primeira nota'))
nota2 = int(input(''))