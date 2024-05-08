# Entrada de dados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Cálculos
adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Tratamento da divisão por zero
if num2 == 0:
  divisao = "Erro: Divisão por zero!"
else:
  divisao = num1 // num2  # Uso do operador // para divisão inteira

# Exibição dos resultados
print(f"Resultado da Adição: {adicao}")
print(f"Resultado da Subtração: {subtracao}")
print(f"Resultado da Multiplicação: {multiplicacao}")
print(f"Resultado da Divisão: {divisao}")