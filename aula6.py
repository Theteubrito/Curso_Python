'''
Converção de tipos
tambem chamados:
coerção, type convertion, typecasting e coercion.

É o ato de converter um tipo em outros tipos imutaveis e primitivos.

type imutaveis e primitivos:
str, int, float e bool.

Ex:
'''
print(   int('1') + 1   ) # ¬
# a palavra 1 está sendo convertida para o numero 1 e logo em seguida esta sendo somado a mais 1

print (   float(10)   ) # ¬
#o numero Int esta sendo convertido para float

print (str(11) + 'b') # ¬
''' o número int está sendo convertido para str e, logo em seguida, sendo CONCATENADO a letra b

Neste exemplo, o paython por ser uma linguagem dinâmica, ele está usando a programação de polimorfismo,
onde um simbolo matemático q significa soma, está ganhando outro siginificado, o de concatenação.
Juntando assim, os dois argumentos.
'''

print(   bool('')   ) # ¬
# a str vasia esta sendo convertido para bool q, por padrao é False (o padrao sempre será False)
# mas se for adicionado algo, como por exenplo um espaço, tornasse True
print(   bool(' ')   )