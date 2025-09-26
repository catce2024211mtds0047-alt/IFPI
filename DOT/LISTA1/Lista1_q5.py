def peso_ideal(altura, sexo):
    if sexo == 2:
        return (72.7 * altura) - 58
    elif sexo == 1:
        return (62.1 * altura) - 44.7


while True:
    try:
        Sexo = int(input("Digite o sexo (FEMININO - 1 / MASCULINO - 2): "))
        if Sexo in [1, 2]:
            break
        else:
            print("Por favor, digite 1 para FEMININO ou 2 para MASCULINO.")
    except ValueError:
        print("Por favor, digite um NÚMERO válido para o sexo.")
while True:
    try:
        Altura = float(input("Digite a altura em metros: "))
        if Altura > 0 and Altura <= 3.5:
            break
        else:
            print("Por favor, digite uma altura válida entre 0 e 3.5 metros.")
    except:
        print("Altura inválida. Tente novamente.")

peso = peso_ideal(Altura, Sexo)
print(f"O peso ideal é: {peso:.2f} kg")
