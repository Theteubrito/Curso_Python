# Operadores Logicos Part.1
'''
Operador and (e)

1- No "end" todas as condiçoes precisao ser verdadeiras pra retornar true.

2- Se qualquer valor for considerado falso, a expressão inteira sera avaliada naquele valor.
    - seguindo a logica do fluxo de leitura do codigo, assim como no flux do "If/elif/else". o codigo
      ler as condições e irar parar naquela (false) q nao atende o exigido e nao ira ler as demais q 
      vier a seguir. (Isso faz com q o codigo economise recurso). Por isso a expreção inteira sera 
      avliada apartir da ultima leitura feita.

3- São considerados falsy(algumentos pseudo falsos) :
    - 0 (zero)
    - 0.0 (zero bool)
    - ''(str vazia)
    (todas essas ja foram vistas nas aulas anteriores, porem tem mais.)

4- Tambem existe o tipo "None" que é usadopra representar um nao valor (nem false e nem True)
'''

# 1
print('1')
print (  True and True  ) # verdareiro e verdadeiro == verdadeiro
print (  True and False ) # verdareiro e Falso == Falso
print ( False and False ) # Falso e Falso == Falso

# 2
print('2')
print (   True and True and True  ) # verdareiro e verdadeiro e Verdadeiro == verdadeiro
print (  True and False and True  ) # verdareiro e Falso == Falso
print (  False and False and True ) # Falso == Falso
print (  True and True and False  ) # verdareiro e verdadeiro e Falso == Falso

# 3
print('3')
print (  True and 0   ) # verdareiro e Falso == Falso (O retorno sera: 0)¬
print (bool(True and 0)) #(O retorno sera: False)

print (  True and 0.0 ) # verdareiro e Falso == Falso (O retorno sera: 0.0)¬
print ( bool(True and 0.0)) #(O retorno sera: False)

print ( False and ''  ) # verdareiro e Falso == Falso (O retorno sera: false)



# 4
print('4')
print ( None and None ) # nemum e nemum == nemum (O retorno sera: None)