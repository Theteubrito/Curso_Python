# Operadores Logicos Part.4
'''
Operador in / not in (esta em/ nao esta em)

1- Antes de tudo. Strings sao ITERÁVEIS
    - Significa q, cada letra de uma str, no python, é tratada como um objeto. Sendo asSim, uma str pode 
     ser observada como uma lista de letras. Dito isso é possivel checar (usando in) ou buscar letra por 
     letra (usando []).
     Isso pode ser feito tanto de modo crescente, começando pelo "0", como de maneira decrescente, de modo
     q sempre termine em "-1".

2- O operador "in" é usado para checar se uma condição está dentro de uma lista. Ou se nao está no cado 
do "not in".
'''

# 1
#  0  1  2  3  4  5  6
#  M  A  T  H  E  U  S
# -7 -6 -5 -4 -3 -2 -1
nome = 'MATHEUS'
print(nome[0] ) # M
print(nome[-7]) # M

print(nome[4] ) # E
print(nome[-3]) # E


# 2
nome = input('digite seu nome: ')
procura = input('Oq vc procura no nome digitado?: ')

if procura in nome:
    print(f'"{procura}" está em "{nome}".')
else:
    print(f'"{procura}" não está em "{nome}".')