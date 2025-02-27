# Tipo str(string) - introdução aos tipos de dados
'''
1- Python
    - Python é uma Linguagem de programação de tipagem dinâmica e forte.

2- tipagem
    - refere-se ao sistema de regras que define como os tipos de dados (como números, textos, booleanos, 
    etc.) são tratados e manipulados dentro dessa linguagem. É um conceito fundamental que afeta a forma 
    como os programas são escritos, entendidos e executados.

        - Dinâmica:
            - A verificação de tipos é feita em tempo de execução, ou seja, durante a execução do programa.
            - Oferece maior flexibilidade, pois os tipos das variáveis podem mudar dinamicamente.
            - No entanto, erros de tipo podem ocorrer durante a execução, o que pode levar a falhas inesperadas.

        - Tipagem Forte:
            - A linguagem não permite conversões implícitas entre tipos incompatíveis(str para int).
            - Isso garante maior segurança e evita erros de tipo inesperados.

3- str (Striing)
    - é um dado de texto. Ele tem q estar entre aspas simples ou duplas para ser reconhecido como uma str.
    (DocString tambem é srt)

4- "\"(Escape)
    - caractere usado para fazer o cacartere seguinte ser pulado. Usado em caracteres reservados para 
    permitir a exibição deles em textos.

5- r
    - Usado para exibir expreçoes regulares.

EX:
'''
# 2
print('Ola mundo')
# ele identificou altomaticamente q o argumento recebido é do tipo str


# 3
#Aspas Simples
print('Matheus')
print('"Matheus"')
#Aspas Duplas
print("Matheus")
print("'Matheus'")

# 4
print("\"Matheus\"")

# 5
print(r"\"Matheus\"")