# exercicio
'''
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    exiba:
        seu nome é 
        seu nome invertido é
        seu nome contem (ou nao espaços)
        seu nome tem {n} letras
        A primeira letra do seu nome é
        a Ultima letra do seu nome é

Se nada for digitado em nome ou idade:
    exiba:
        Desculpe, você deixou campos vazios"

'''
# r ¬
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Sua idade é: {idade}')
    print(f'Seu nome invertido é: "{nome[::-1]}"')
   
    if ' ' in nome :
        print('Seu nome tem espaço')
    else:
        print('Seu nome não tem espaço')
    
    if len(nome) <= 1:
        print(f'seu nome tem apenas uma letra')
    else:
        print(F'Seu nome tem {len(nome)} letras')
    
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print('Desculpa, você deixou campos vazios')