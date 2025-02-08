# introdução as f-strings (formatação de string)
'''
Usar o f antes de uma string ativa a formatação da mesma. Permitindo, por exemplo, a marcação
de variaveis.
O uso de {} indica uma variavel dentro da str.

Ex:
'''
nome ='Matheus'
altura = 1.72
peso = 82.0
imc = peso / (altura * altura)


linha_1 = f'{nome} tem {altura:.2f} de altura.'
linha_2 = f'Pesa {peso} quilos, e seu IMC é de {imc:.2f}.'
# o :.2f indica a quantidade de casas decimais haverá no float apos o ponto

print(linha_1)
print(linha_2)