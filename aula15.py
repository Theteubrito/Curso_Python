# input
'''
Input é uma função q solicita dados do usuario.
O codigo ficara parado na linha de codigo do input esperando o usuario interagir e nao finalizara enquato 
isso nao acontecer.

ex:
'''
#nome = input('Qual o seu nome? ') # o input está guardando o dado recebido na variavel
#print(f'seu nome é: {nome}')

'''
É importante saber q, a informação recebida pelo input sempre sera um str. Isso pode quebrar o cadigo 
dependendo do que se deseja fazer com  os dados coletados.

Ex
'''
nu_1 = input ('digite um numero: ')
nu_2 = input('digite outro numero: ')

print(f'a soma dos dois numero é {nu_1+nu_2}')
# os numeros coletados serão concatenas ao em vez de somados por serem str.

'''
ATENÇÃO!!!!

Nos dois exemplos demonstrados anteriortmente, nem um deles tem verificação de dados coletados.
No primeiro exemplo:
Pede um nome. nada impede o usuario retornar um numero.

No segundo exemplo:
O codigo pede um numero, e mesmo q o dado seja transformado em int ou 
float ( nu_1 = int(input ('digite um numero: ')) ) para resolver o problema da concatenação. Como nao 
ha uma checagem, se o usuario entrar com uma str o codigo será quebrado.
'''
