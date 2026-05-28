# Estrutura Condicional e Repetição

# Operadores Lógicos
# && (E)
# || (OU)
# ! (Negação)

# Operadores de Comparação
# == (Igualdade)
# != (Desigualdade)
# > (Maior que)
# < (Menor que)
# >= (Maior ou igual a)
# <= (Menor ou igual a)

# Estrutura Condicional

# variável = valor da variável

# if variavel, condição, valor:
#     print("Mensagem")
# else:
#     print("Mensagem")

idade = 18

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

    
# Estrutura de Repetição

# for contador in range(valor):
#     print("Mensagem")

for i in range(5): # A letra I é a variável contadora, onde ela vai incrementar até 5.
    print("Olá mundo!") # Mostra a mensagem 5 vezes.

for i in range(10): # A letra I é a variável contadora, onde ela vai incrementar até 10. Porém antes do 10 (por exemplo 9) ela para.
    print(i)

for i in range(10): # A letra I é a variável contadora, onde ela vai incrementar até 10. Porém antes do 10 (por exemplo 9) ela para.
    if(i == 5):
        break # Quebra o loop.
    print(i)


for i in range(10): # A letra I é a variável contadora, onde ela vai incrementar até 10. Porém antes do 10 (por exemplo 9) ela para.
    if(i == 5):
        continue # Pula o número 5.
    print(i)