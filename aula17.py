# Condicionais Parte 2 - Entendendo o fluxo
'''
É importante sailientar q, em um bloco condicional, sera execultado o cript da primeira condição 
atendia, e todas as demais condiçoes do mesmo bloco serao ignoradas, mesmo q tenham suas condiçoes tambem 
atendidas.


'''

condicao1 = False
condicao2 = False
condicao3 = False

#-------------------------------------BLOCO CONDICIONAL-----------------------------------------------
if condicao1 :
    print ('condição 1 foi atendida.')
    print(
        'entao, todas as demais condições deste bloco, mesmo q tenham suas condiçoes' 
        'atendidas serão ignoradas'
        )

elif condicao2 :
    print ('condição 2 foi atendida.')
    print(
        'entao, todas as demais condições deste bloco, mesmo q tenham suas condiçoes' 
        'atendidas serão ignoradas'
        )

elif condicao3 :
    print ('condição 3 foi atendida.')
    print(
        'entao, todas as demais condições deste bloco, mesmo q tenham suas condiçoes' 
        'atendidas serão ignoradas'
        )
# O else nao recebe condiçao pos ele é a exeção das demais condiçoes 
# (se as anteriores nao foram atendidas entao...)
else:
    print (' nem uma das consicoo de 1 ate a 3 foram atendidas')
#-------------------------------------------FIN DO BLOCO----------------------------------------------


print('fora do primeiro bloco')


#---------BLOCO CONDICIONAL----------
if 10 == 10:
    print('Outro if')
#----------FIN DO BLOCO--------------


print('fora do segundo bloco')