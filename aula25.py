# Interpolação de strings básica
'''
A interpolação é uma forma de formatação de str assim como o "f str" e o "format".
Na interpolação se usa o sinal de % seguido do símbolo q referencia o tipo do dado q deve ser adicionado
a str final.

  simb ---- tipo
   s   ---- str
d ou i ---- int
   f   ---- float
   x   ---- Hexadecimal minúsculo
   X   ---- Hexadecimal maiúsculo

Ex:
'''
nome = 'Matheus'
preco = 1000.556367478

variavel_1 = '%s, o preço total foi de R$ %f' %(nome, preco) 
print(variavel_1)

# É possivel usar a "retração" das casas decimaia, tambem, igual as formas de formatação vistas antes.
# usando "." sequido da quantidade de casas decimais desejadas antes do f (referente ao float).
variavel_2 = '%s, o preço total foi de R$ %.2f' %(nome, preco) 
print(variavel_2)




# Hexadecimal
'''
Números hexadecimais são números que usam 16 símbolos, de 0 a 9 e A a F, para representar valores. 
É um sistema de numeração posicional de base 16, muito usado na computação e na web.

Numeros hecadecimais, geralmente tem 4 ou 8 casas, para isso, usa-se "04" ou "08" antes do x para 
determinar o numero de casas geradas.

Ex:
'''
# usando i para referenciar int, 04 para o numero de casas e x minusculo para gerar hexadecimal minúsculo
print('O hexadecimal de %i é %04x' % (15, 15))

# usando d para referenciar int, 08 para o numero de casas e x maiusculo para gerar hexadecimal maiúsculo.
print('O hexadecimal de %d é %08X' % (15, 15))