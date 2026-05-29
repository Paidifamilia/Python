# Funções em Python

# Definição de Função

# def nome_da_funcao():
#     print("Hello World!")

# print(nome_da_funcao()) # Chamando a função
# print(nome_da_funcao("parametro")) # Chamando a função com parâmetros.

# Função sem parâmetros
def saudacao():
    print("Olá, seja bem vindo!")

saudacao() # Execução

# Função com parâmetros
def saudacao(nome):
    print("Olá", nome, "seja bem vindo!")

saudacao("Murilo")

# Podendo ser assim:

# def saudacao(nome):
#     print(f"Olá {nome}, seja bem vindo!")

# saudacao("Murilo")

def soma(a, b):
    print(a + b)

soma(10, 20)

# Retorno de funções
# return

def soma(a, b):
    return a + b

print(soma(10, 20))

# Retorno de múltiplas variáveis
def operacoes(a, b):
    return a + b, a - b, a * b, a / b

soma, sub, mult, div = operacoes(10, 20)
print(f"Soma: {soma}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")