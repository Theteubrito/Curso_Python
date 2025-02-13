# Operadores Logicos Part.2
'''
Operador or (ou)

1- No "or" qualquer condição verdadeira avalia toda a expressão como verdadeira.

2- Se qualquer valor for considerado verdadeiro, a expressão inteira sera avaliada naquele valor.
    - Isso é chamado de avaliação de curto circuito.
'''

# 1
print ('1')
print(  True or False ) # True
print( False or True  ) # True
print( False or False ) # False

# 2
print ('2')
print(  True or False or True ) # True (o retorno sera: True )

print( False or   1   or True ) # True (o retorno sera: 1 )¬
print(bool (False or 1 or True)) # True

print( False or False or  ''  ) # False (o retorno sera: '' )¬
print( bool(False or False or'')) # False