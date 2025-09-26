import math

# Função para calcular a área do círculo


def area(raio):
    """
    Calcula a área de um círculo dado seu raio.

    Args:
      raio: O raio do círculo (número real).

    Returns:
      A área do círculo (número real).
    """
    return math.pi * raio ** 2

# Função para calcular o perímetro do círculo


def perimetro(raio):
    """
    Calcula o perímetro de um círculo dado seu raio.

    Args:
      raio: O raio do círculo (número real).

    Returns:
      O perímetro do círculo (número real).
    """
    return 2 * math.pi * raio

# --- Lógica principal do programa ---


# Lê o raio do usuário e converte para um número real
try:
    raio_circulo = float(input("Digite o raio do círculo: "))

    # Chama as funções para calcular a área e o perímetro
    area_circulo = area(raio_circulo)
    perimetro_circulo = perimetro(raio_circulo)

    # Imprime os resultados formatados
    print(f"\nÁrea do círculo: {area_circulo:.2f}")
    print(f"Perímetro do círculo: {perimetro_circulo:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
