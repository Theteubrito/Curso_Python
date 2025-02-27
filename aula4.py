# Tipagem int e float - Introdução aos tipos de dados
'''
1- int (Numero Inteiro)
    - O tipo int representa qualquer numero inteiro, positivo ou negativo.
    (int sem sinal é considerado positivo)

2- float (ponto flutuante)
    - O tipo float representa qualquer numero com ponto flutuante, positivo ou negativo.
    (float sem sinal é considerado positivo)

3 - type
    - A função(na verdade é uma metaclasse) type mostra o tipo q o pythom inferiu ao argumento recebido.

EX:
'''
# 1
print(11) # int
print(-11) #int

# 2
print(1.1) # float
print(-1.1) # float

# 3
# str ¬
print(   type('Matheus')   )

# int ¬
print(   type(11)   )
print(   type(-11)   )

# float ¬
print(   type(1.1)   )
print(   type(-1.1)   )