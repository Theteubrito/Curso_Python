# exercicio

print('Vamos brincar um pouco')
print()

palavra = input('Gidite uma palavra ->  ')

caracteres = len(palavra)

letra = 0
nova_palavra = '*'

while letra < caracteres:
    if (palavra[letra]) != ' ':
        nova_palavra += f'{palavra[letra]}*'
    else:
        nova_palavra += f'---*'
    letra += 1
print(nova_palavra)