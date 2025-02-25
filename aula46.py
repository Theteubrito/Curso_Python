# Tudo q apendemos em while funciona no for(continue, break, else, etc..)

for n in range(10):
    if n == 2:
        print('nao vou mostrar o 2')
        continue
    if n == 8:
        print(f'{n=} entao seu for será quebrado!')
        break
    
    for colunas in range(1, 3):
        print(n, colunas)
else:
    print('For execultado com sucesso!')