print("desafio 1: Divisão ---")
try:
    numerador = int(input("digite o numerador: "))
    denominador = int(input("digite o denominador: "))
    resultado = numerador / denominador
    print(f"O resultado da divisão é: {resultado}")
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")
except ZeroDivisionError:
    print("Erro: O denominador não pode ser zero.")
except Exception as erro:
    print(f"erro inesperado: {erro}")
else:
    print(f"sucesso! Resultado: {resultado}")
finally:
    print("Fim da divisão--")
