# Introdução ao try except
'''

1- Exceção
    Em Python, uma exceção é um evento que ocorre durante a execução de um programa que interrompe o fluxo 
    normal das instruções. Quando uma exceção ocorre, Python cria um objeto de exceção e passa esse objeto 
    para o sistema de gerenciamento de exceções, que tenta encontrar um manipulador adequado para tratar 
    essa exceção.  (Explicação tirado do copiloto)
    Em resumo, uma exceção é um erro de coódigo.

2 -
Try --- Tentar execultar
except --- Ocorreu algum erro ao tentar executar

Ex:
'''

#  1  O codigo abaixo vai gerar uma exceção (str nao podem ser convertidas para int)
#str = 'a'
#print(f'O numero é: {int(str)}')

'''
a exceção gerada foi
ValueError: invalid literal for int() with base 10: 'a'
'''