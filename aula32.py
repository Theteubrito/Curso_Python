# Exercicios
'''
Exercicio 1
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
#R1
'''
print('É PAR OU IMPAR? VAMOS DESCOBRIR!')
nu_int = input('Digite um numero inteiro -> ')
try:
    nu_int = int(nu_int)
    resto = nu_int % 2

    if resto == 0:
        print(f'O número {nu_int} é Par')
    else:
        print(f'O número {nu_int} é impar')
except:
    print('você nao digitou um número válido')
'''

'''
Exercicio 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
#R2
'''print('QUAL A SALDAÇÃO?')
print()
print('apenas a hora, sem os minutos')
hora = input('Que horas são?-> ')
try:
    hora =(int(hora))
    if (hora >= 0) and (hora <= 11):
        print('Bom dia!')

    elif(hora >= 12) and (hora <= 17):
        print('Boa Tarde!')

    elif (hora >= 18) and (hora <= 23):
        print('Boa noite!')

    else:
        print('Voê nao informou um horario Válido')

except:
    print('Voê nao informou um horario  Válido')
'''

'''
Exercicio 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''
#R3
'''
print('SEU NOME É GRANDE?')
print()

nome = input('Digite seu primeiro nome -> ')
cacacteres = len(nome)

if cacacteres <= 0:
    print("Você nao digitou seu nome.")

elif cacacteres <=4:
    print('Seu nome é pequeno.')

elif (cacacteres == 5) or (cacacteres == 6):
    print("Seu nome é normal.")

else:
    print("Seu nome é muito grande!")
'''

