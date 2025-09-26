def resultado(n1, n2):
    media = (n1+n2)/2
    print(f"A média semestral é: {media:.2f}")
    if media >= 6:
        return print("Aprovado")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
resultado(nota1, nota2)
