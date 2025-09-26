def par_impar(x):
    if x % 2 == 0:
        return True
    else:
        return False


num = int(input("digite um numero:"))
if par_impar(num):
    print("O numero é par")
else:
    print("O numero é impar")
