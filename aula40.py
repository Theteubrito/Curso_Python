OP_VALIDOS = '+-/*'

print('Calculadora')
print('Operadores-> + - * /')
print('-------------------------')
print('')
while True:
    n1 = 0
    n2 = 0
    operacao = 0
    op = ''
    n_v = None
    op_v = None

    n1 =input('Primeiro número -> ')
    try:
        n1 = int(n1)
        n_v = True
    except:
        n_v = None

    if n_v is True:
        n2 = input('Segundo número-> ')
        try:
            n2 = int(n2)
        except:
            n_v = False
    else:
        print ('Numero inválido')

    if n_v is True:
        op = input('Operador-> ')
        if op in OP_VALIDOS:
            op_v = True
        else:
            print ('Operador Inválido')
    elif n_v is False:
        print ('Numero inválido')


    if op_v is True:
        if op == '+':
            operacao = n1 + n2
            print (f'{n1} + {n2} = {operacao}')
        
        elif op == '-':
            operacao = n1 - n2
            print (f'{n1} - {n2} = {operacao}')
        
        elif op == '*':
            operacao = n1 * n2
            print (f'{n1} * {n2} = {operacao}')
        
        else:
            operacao = n1 / n2
            print (f'{n1} /. {n2} = {operacao}')

    sair = input('[S}air? (pra continuar aperte enter)-> ').lower().startswith('s')
    if sair is not True:
        print('-------------------------')
        print('')
        continue
    else:
        break
