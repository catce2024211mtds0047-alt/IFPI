import math


def fatorial(num):
    return math.factorial(num)


while True:
    try:
        numero = int(input("Digite um número para calcular o fatorial: "))
        if numero < 0:
            print("Por favor, digite um número maior que zero.")
        else:
            numero = fatorial(numero)
            print(f"O fatorial é : {numero}")
    except:
        print("Valor inválido. Tente novamente.")
    print("Deseja continuar? (S/N)")
    continuar = input().strip().upper()
    if continuar != 'S':
        break
