# while + while (laço interno)
'''
ATENÇÃO ISSO VAI SER CONFUSO!!!
'''
QUANTI_LINHAS = 5
QUANTI_COLUNAS = 5

linha = 1

while linha <= QUANTI_LINHAS:
    coluna = 1
    while coluna <= QUANTI_COLUNAS:
        print (f'{linha=} {coluna=}')
        coluna += 1
    print('')
    linha += 1

print('Acabou!')

'''
DESCREVENDO O FLUXO:


# LAÇO 1
linha é igual 1

enquanto 1 for menor ou igual a 5 (true):
    coluna igual a 1
    enquanto 1 for menor ou igual a 5 (true):
        printa
        coluna mais 1 (2)

        
# LAÇO 2        
linha é igual 1

enquanto 1 for menor ou igual a 5 (true):
    coluna igual a 2
    enquanto 2 for menor ou igual a 5 (true):
        printa
        coluna mais 1 (3)

        
# LAÇO 3
linha é igual 1

enquanto 1 for menor ou igual a 5 (true):
    coluna igual a 3
    enquanto 3 for menor ou igual a 5 (true):
        printa
        coluna mais 1 (4)


# LAÇO 4
linha é igual 1

enquanto 1 for menor ou igual a 5 (true):
    coluna igual a 4
    enquanto 4 for menor ou igual a 5 (true):
        printa
        coluna mais 1 (5)

        
# LAÇO 5
linha é igual 1

enquanto 1 for menor ou igual a 5 (true):
    coluna igual a 5
    enquanto 5 for menor ou igual a 5 (true):
        printa
        coluna mais 1 (6)

        
# LAÇO 6
linha é igual 1

enquanto 1 for menor ou igual a 5 (true):
    coluna igual a 6
    enquanto 6 for menor ou igual a 5 (false):
    (resto do codigo ignorado)
printa ''
linha mais 1 (2)


# LAÇO 7
linha é igual 2

enquanto 2 for menor ou igual a 5 (true):
    coluna igual a 1
    enquanto 1 for menor ou igual a 5 (true):
        printa
        coluna mais 1 (2)

....


# LAÇO 29
linha é igual 5

enquanto 5 for menor ou igual a 5 (true):
    coluna igual a 6
    enquanto 6 for menor ou igual a 5 (false):
        (Resto od codigo ignorado)
    printa ' '
    linha mais 1 (6)

    
# LAÇO 30
enquanto 6 for menor ou igual a 5 (false):
    (Resento do codigo ignorado)
print 'Acabou!'
'''
