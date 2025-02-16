# Fatiamento de strings
'''
1- Como ja foi visto antes, uma sting, no python, se comporta como uma lista. e se pode visitar cada caractere
usando a sua posição. Sendo 0, 1, 2, 3, ... da esqueda para a direita e ... -3, -2, -1 da direta 
para a esquerda.
ex:
  ->
  012345678
  Olá mundo
 -987654321
         <-

2- Fatiamento [i:f:p] [::]
  O fatiamento, é exatamento oq o nome diz, ele fatia uma string
    i: --- inicio
    :f --- fim
    :p --- passos (pula caracteres)

3- len é uma função q retorna a quantidade de objetos em uma lista
'''

variavel ='Olá mundo'

# 1
print(variavel[ 5])
print(variavel[-4])


#2
# i:f
print(variavel[0:5]) # i:f inicia no 0 e mostra ate o caracter antes do 5
print(variavel[:5]) # i:f com inicio omitido q significa q serão todos os caracteres azntes do o 4
print(variavel[4:9]) # i:f
print(variavel[4:]) # i:f com o fim omitido q significa q serão todos os caracteres apos o 4
# ::p
print(variavel[::1]) # o primeiro caracter a cada 1 passos ([O][l][á][][m][u][n][d][o] => 'Olá mundo')
print(variavel[::2]) # o primeiro caracter a cada 2 passos ( [Ol][á ][mu][nd]o => 'oámno')
print(variavel[::3]) # o primeiro caracter a cada 3 passos ( [Olá][ mu][ndo] => 'o n')
print(variavel[::4]) # o primeiro caracter a cada 3 passos ( [Olá ][mund]o => 'Omo')


#3
print(len(variavel))