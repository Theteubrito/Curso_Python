# Esse exercicio foi sugerido pelo Gemini
'''
crie um progrma que converta temperatura de Celsius para Fahrenhit. O usuario deve inserie a temperatura 
em Celsius e o programa deve exibit a temperatura equivalente em Fahrenhit.

Formula
Fahrenhit = (Celsius * 9/5) + 32
'''

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
simbolos = "'´`~^{[}]?/°,.:;|!@#$%¨&*()_+=§'" 

print('Conversor de C° para F°')


celsius =input('Qual a temperatura em C° ? ')

if (celsius not in alfabeto) and (celsius not in simbolos):
    #celsius =(float(celsius))
    fahrenhit = ((float(celsius)) * 9/5) + 32

    print(f'{celsius} C° para Fahrenhit é {fahrenhit} F°')
else:
    print('vc nao digitou um número válido!')