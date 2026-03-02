num = []

maior = 0

for i in range(3):
    valor = int(input("Digite um número: "))
    num.append(valor)

    if i == 0:
        maior = valor
    elif valor > maior:
        maior = valor
    
print("O maior número é: ", maior)