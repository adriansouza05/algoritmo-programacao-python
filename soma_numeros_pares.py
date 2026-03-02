soma = 0

for i in range(101):
    if i % 2 == 0:
        soma += i

print(f"A soma de todos os pares 1 a 100 é = {soma}")

#ou podemos fazer assim:
soma = sum(range(0, 101, 2))
print(soma)