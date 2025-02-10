# Condicionais
'''
if /    elif   / else
se / se nao se/ se nao

O consdiciomanento é uma blocagem de codigo onde se exige uma condição para ser execultado.
Ele faz uma pergunta ao codigo, retornando como resposta um bool (true ou false).
Entao, se a condição nao for atendida (a resposta da pergunta feita for false) o codigo 
dentro dela sera ignorado e passado para o resto do script abaixo.
Caso a condição seja atendida (a reposta da pergunta feita for true), o codigo execultara sua blocagem 
condicionada e ao fim, seguirar para o resto do codigo fora do bloco.


É IMPORTANTE SABER -----------------------------------------------------------------

-O if é idependente do elif e do else, e nao pode se repetir em um questionamento.

-O elif depende do if para existir e do else, e pode se repetir varias vezes no 
mesmo questionamento.

-O else depende do if, mas nao do elif para existir, e nao pode se repetir 
em um questionamento.
------------------------------------------------------------------------------------
Ex:
'''

entrada = input('Voce deseja entrar ou sair? ')

if entrada == 'entrar':
    print('vc entrou no sistema')

elif entrada == 'sair':
    print('voce saiu do sistema')

else:
    print('vc nao digitou entrar e nem sair')


print('fora do bloco condicionado')