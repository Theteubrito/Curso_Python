# Operadores de atribuição com operadores aritméticos
'''
=   ---- Atribuição 
+=  ---- ele mesmo mais ou concatenação
-=  ---- ele mesmo meno
*=  ---- ele mesmo vezes ou repetição
/=  ---- ele mesmo dividido por (com poto flutuante)
//= ---- ele mesmo dividido por (divisãointeira)
**= ---- ele mesmo elevado a
%=  ---- o resto da divisão dele mesmo por

Ex:
'''
# =
contador = 10
str = 'a'

# +=
contador = 10
str = 'a'
contador += 1
str += 'b '
print(contador)
print(str)

# -=
contador = 10
contador -= 1
print(contador)

# *=
contador = 10
str = 'a'
contador *= 2
str *= 10
print(contador)
print(str)

# /=
contador = 10
contador /= 2
print(contador)

# //=
contador = 10
contador //= 2
print(contador)

# **=
contador = 10
contador **= 2
print(contador)

# %=
contador = 10
contador %= 2
print(contador)