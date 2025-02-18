# Introdução ao try except
'''

1- Exceção
    Em Python, uma exceção é um evento que ocorre durante a execução de um programa que interrompe o fluxo 
    normal das instruções. Quando uma exceção ocorre, Python cria um objeto de exceção e passa esse objeto 
    para o sistema de gerenciamento de exceções, que tenta encontrar um manipulador adequado para tratar 
    essa exceção.  (Explicação tirado do copiloto)
    Em resumo, uma exceção é um erro de coódigo.

2 - Try / except é muito parecidos com o if / else. Mas, enquanto o if / else crial um fluxo de codigo 
condicionado. o Try / except evita do codigo ser quebrado.

   Try --- Tentar execultar
except --- Ocorreu algum erro ao tentar executar

Ex:
'''

# 1  O codigo abaixo vai gerar uma exceção

# int('a') #(str nao podem ser convertidas para int)

#a exceção gerada foi ¬
#Traceback (most recent call last):
#  File "c:\Users\mathe\OneDrive\Documentos\GitHub\Curso_Python\aula29.py", line 20, in <module>
#    int('a') #(str nao podem ser convertidas para int)
#    ~~~^^^^^
#ValueError: invalid literal for int() with base 10: 'a'

# 2
try:
    print ('    entrou no try')
    int ('a')

except:
    print('    entrou no except')
    print('Não é possivel converter letra para digito')
'''
Em ves do codigo explodir uma exceção (quebrar, da erro). O codigo pulou para o except (igual quando 
uma condição do if nao é atendida e pula para o else).
'''
'''
ATENÇÃO!!!
Nesse trecho do codigo:
try:
    print ('    entrou no try')
    int ('a')

Em uma situação real, é mais prudente por a condição q pode gerar a exceção em primeiro. No nome 
desse conceito é "Fast fail". isso permite o codigo ser mais rapido e poupa tempo.
sendo assim:
try:
    int ('a')
    print ('    entrou no try')
'''