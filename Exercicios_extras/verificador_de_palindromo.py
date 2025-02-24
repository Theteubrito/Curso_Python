# Exercicio sugerido pelo Gemini
'''
Crie um programa que peça ao usuário para inserir uma palavra ou frase e determine se ela é um palíndromo (ou seja, se a palavra ou frase é a mesma lida da esquerda para a direita e vice-versa, desconsiderando espaços e letras maiúsculas ou minúsculas).

Exemplo
-"ovo" é um palíndromo
-"Python" não é um palíndromo
-"A man, a plan, a canal: Panama" é um palíndromo

Dicas
-Converta a entrada do usuário para letras minúsculas usando o método lower().
-Remova os espaços da entrada do usuário usando o método replace(" ", "").
-Compare a string original com sua versão invertida.
'''

print('Verificador de palindromo')
print('')

palavra = input('Digite uma palavra ou fraze -> ').lower().replace(' ','').replace('.','')
inverco = palavra[::-1]

if palavra == inverco:
    print('Esta palavra é um Palíndromo')
    print(f'"{palavra}" = "{inverco}"')
else:
    print('-' * 10)
    print('Esta palavra não é um Palíndromo')
    print(f'"{palavra}" =/= "{inverco}"')    