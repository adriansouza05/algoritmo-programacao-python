num = int(input("Informe um número: "))

while(num != 0):

    for i in range(11):
        resul = num * i
        print(f"{num} x {i} = {resul}")
    num = int(input("\nInforme outro número (0 para sair): "))