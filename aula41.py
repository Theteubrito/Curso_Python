#while/else
'''
o While pode ter um else. Ele é execultado apos o fim do laço de repetição chegar ao fim. se ouver uma 
condição no meio do laço de repetição q de um break no laço, o else nao é execultado.

Ex:
'''

str = ('Valor qualquer')

i = 0

while i < len(str):
    print(f'{str[i]}')

#    if str[i] == ' ':
#        break

    i += 1
else:
    print( 'Fim do laço')

print('Fora do laço')
