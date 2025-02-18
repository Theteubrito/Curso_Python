# Variaveis, Constantes e complexidade de codigo part. 1
'''
-1 CONSTANTE = "variavis" que não vão mudar.
     Em outras linguagem de programação a diferença entre variavel e constante é bem definida. No Python, 
     essa diferença não existe de fato. Mas, para diferenciar uma constante de uma variavel, para melhorar
     a legibilade do codigo, a leitura e deixar tudo menos complexo de entender. Ou seja, uma "boa pratica"
     constantes são escritas em letras maiusculas. para q assim outras pessoas entendam q aquilo é uma 
     constante, e seu valor não deve ser alterado.

BOAS PRATICAS
    Quando se escreve um codigo, devemos prezar pela SIMPLICIDADE, pelo MENOS É MAIS. Um bom codigo é facil
    de entender, de ser lido por terceiros. Um codigo complexo de mais é RUIM.

- 2 Muitas condições no mesmo if  --> RUIM
    Ter muitas condiçoes em um unico if, muitos operadore logicos, deixa o entendimento do que aquele if 
    está condicionado dificil de entender. Exigindo q ele seja lido e testado para ser compreendido. UM 
    BOM CODIGO PRECISA DE UMA UNICA LEITURA PARA SE FAZER ENTENDER.
    Por isso, se um resultado precisa de muitas consicionais, é melhor usar mais ifs do que mais operadores
    logicos.

-3 Muita identação --> RUIM
     Codico com muita hierarquia, muita identação tornace um dcodico complexo, dificil de entender. e isso
     tambem é RUIM. Tem q se evitar ao maximo.

'''
# carro 
c_velocidade = 61 # velocidade do carro
c_localizacao = 90 # ponto inicial onde o carro está

# radar
R_VEL_PERMITIDA = 60 # Velocidade permitida pelo radar 60kh
R_LOCALIZACAO = 100 # ponto onde o radar está
R_RANGE = 1 # a distancia de leitura q o radar alcansa (tanto a sua frente, q uando atas dele)

'''
|_ _ _ _ _ _ _ _ _ _ CARRO _ _ _ _ _ _ _ _ _ _ _ _ ~ RADAR ~ _ _ _ _ _ _ _ _ _ _|
|ESTRADA            | 90  |                       |R||100||R|            ESTRADA|
'''




# Variaveis, Constantes e complexidade de codigo part. 2

if c_localizacao >= (R_LOCALIZACAO - R_RANGE) and c_localizacao <= (R_LOCALIZACAO + R_RANGE):
    print('O carro foi visto pelo radar')
    if c_velocidade > R_VEL_PERMITIDA:
        print('Carro foi multado')
    else:
        print('carro não foi multado')
else:
    print('O carro não foi visto pelo radar')


# resumindo e deixando oocdigoa cima mais simples e menos complexo

entrou_no_radar = c_localizacao >= (R_LOCALIZACAO - R_RANGE)
saindo_do_radar = c_localizacao <= (R_LOCALIZACAO + R_RANGE)

c_multado = c_velocidade > R_VEL_PERMITIDA

if entrou_no_radar and saindo_do_radar and c_multado:
    print('Carro foi multado')

else:
    print('carro não foi multado')

