# introdução as f-strings (formatação de string)
'''
1- f
    - Usar o f antes de uma string ativa a formatação da mesma. Permitindo, por exemplo, a marcação
    de variaveis.

2- {} (chaves)
    - O uso de {} indica uma variavel dentro da str.

3 - .: "numero" f
    - indica a quantidade de casas decimais haverá no float apos o ponto flutuante

Ex:
'''
nome ='Matheus'
altura = 1.72
peso = 82.0
imc = peso / (altura * altura)

# 1 e 2
linha_1 = f'{nome} tem {altura} de altura.'

# 3
linha_2 = f'Pesa {peso} quilos, e seu IMC é de {imc:.2f}.'


print(linha_1)
print(linha_2)