# a identidade do valor que está na memoria
'''
1- id ---> Função q retorna o id do objeto
    Quando uma variavel é criado, ela tem seu valor guardado na memoria. Esse valor recebe uma 
    identificação, um id (o Id é o nome real do objeto. O nome de uma variavel é um apelido q vc 
    esta tribuindo ao id). É atraves desse id q o python busca de fato o dado quardado.

2- O python é uma linguagem inteligente. Entao, quando se cria duas variaveis COM O MESMO VALOR 
    LITERAL, pra economizar recursos da maquina, o python nao cria dois valores na memoria. Ele cria apenas
    um vamor (um id) e atridui o mesmo id para as duas variaveis diferentes.

3-  Flags (bandeiras)
    Flags é uma pratica no desenvolvimento de algoritimos utilizada para marcar ações. Pra saber se algo 
    foi feito ou se uma parte do codigo esta sendo visitada. É um feedback.

4 - is e  is not
    Sao operadores relacionais semelhantes ao "==" e "!=". Geralmente sao utilizado com o "None"
      is   ---- é (==)
    is not ---- Não é (!=)


Ex:
'''
# 1
variavel_1 = 'a'
print(id(variavel_1))

# 2
variavel_2 = 'a'
variavel_3 = 'b'
print(id(variavel_1))
print(id(variavel_2))
print(id(variavel_3))

# 3
condicao = True

#----- flag ---
passou_no_if = None
#----- ---- ---

if condicao:
    passou_no_if = True #flag
    pass
else:
    pass

# 4
# is
if passou_no_if is True: # passou_no_if É True (passou_no_if é igual a True)
    print('Passou no if')
else:
    print('Não passou no if')

# is not
if passou_no_if is not None: # passou_no_if NÃO É none (passou_no_if é diferente de none)
    print('Passou no if')
else:
    print('Não passou no if')
