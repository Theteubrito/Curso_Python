# Formatação de str com método format

a ='A'
b = 'B'
c = 1.1

# indexado por ordem dos argumentos(da direita para a esquerda)¬
formato_1 = 'a= {}, b= {}, c= {},'.format(a, b, c)

# indexado pela posição dos argumentos na lista (sempre começa em 0)¬
formato_2 = '{3}, a= {0}, b= {1}, c= {2:.2f},'.format(a, b, c, 'helo')

''' 
Parametro nomeado:
É o nome que se dá a um argumento nomeado. Isso torna seu indexamento mais confiavel.
Todo argumento apos um paramentro nomeado DEVE ser nomeado tambem
EX:
'''
formato_3 = 'a= {nome0}, b= {nome1}, c= {nome2},'.format(nome0=a, nome1=b, nome2=c,)



print(formato_1)
print(formato_2)
print(formato_3)