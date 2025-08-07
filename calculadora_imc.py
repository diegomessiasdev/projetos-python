# Calculadora de IMC
# Autor: Diego Messias
# Data: 2025-08-07
# Descrição: Programa simples para calcular o Índice de Massa Corporal (IMC) e classificar o resultado.

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")

if imc >= 25:
    print("Você está com sobrepeso.")
else:
    print("Você está no peso ideal.")

