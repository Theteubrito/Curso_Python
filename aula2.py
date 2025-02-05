'''
print()
É uma função q recebe um ou mais argumentos.
Serve para imprimir o argumenta na teal de saida
'''
print('argumento')

'''
sep=""
É um argumento NOMEADO da função print, onde se 
seta a separação dos argumentos.
'''
print(1,2,3,4,5) # o separador por padão é " " (espaço)
print(1,2,3,4,5, sep='-') # definindo o serapador para "-" (traço)

'''
Quebra de linha
São os caracteres definidos para a quebra de linha.
sendo eles:
\r\n -> CRLF (sistema windows)
\n -> LF (sistema MacOs)

Onde o \r significa "RETURN"
e o \n significa "LINE FEED"

dito isso...
'''

'''
end=''
É um argumento NOMEADO utiçizado para mudar 
o final do print (sendo o padrao o definido pelo sistema)
'''
print(1,2,3) # o end padrao sendo '\r\n' (quebra de linha)
print(1,2,3, end='FIM') # alterando o end para 'FIM' (uma string)