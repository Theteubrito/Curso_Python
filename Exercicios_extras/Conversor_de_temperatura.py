# Esse exercicio foi sugerido pelo Gemini
'''
crie um progrma que converta temperatura de Celsius para Fahrenhit. O usuario deve inserie a temperatura 
em Celsius e o programa deve exibit a temperatura equivalente em Fahrenhit.

Formula
Fahrenhit = (Celsius * 9/5) + 32
'''

print('Conversor de C° para F°')


celsius = float(input('Qual a temperatura em C° ? '))
fahrenhit = (celsius * 9/5) + 32


print(f'{celsius} C° para Fahrenhit é {fahrenhit} F°')