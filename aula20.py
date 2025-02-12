# Exercicio
'''
crie uma maquina de comparação de valores. Ela tem q pedir ao usuario dois valores, e com esses valores
Ela tem q dizer para o usuario qual valor é maior q o outro ou se sao iguais.
'''
v_1 = input('Diga um valor: ')
v_2 = input('Diga um segundo valor: ')

if v_1 > v_2 :
    print(f'o primeiro valor {v_1}, é maior q o segundo {v_2}')


elif v_1 < v_2 :
    print(f'o primeiro valor {v_1}, é menor q o segundo {v_2}')


else :
    print(f'o primeiro valor {v_1}, é igual ao segundo {v_2}')