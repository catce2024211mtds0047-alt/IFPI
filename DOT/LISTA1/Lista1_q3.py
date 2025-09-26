def celsius(fahrenheit):
    """
    Converte uma temperatura de Fahrenheit para Celsius.

    Args:
      fahrenheit: A temperatura em graus Fahrenheit.

    Returns:
      O valor correspondente em graus Celsius.
    """
    celsius = ((fahrenheit - 32) / 9) * 5
    return celsius

# --- Lógica principal do programa ---


# Solicita a temperatura ao usuário
try:
    temp_fahrenheit = float(
        input("Digite a temperatura em graus Fahrenheit: "))

    # Chama a função e armazena o resultado
    temp_celsius = celsius(temp_fahrenheit)

    # Exibe o resultado com uma formatação simples
    print(f"\n{temp_fahrenheit}°F correspondem a {temp_celsius:.2f}°C.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
