n = int(input("Quantos números você vai digitar: "))
numeros = []

for i in range(n):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

print("VALORES = ", end="")
for i in range(n):
    print(f"{numeros[i]:.1f} ", end="")
print()

soma = sum(numeros)
print(f"SOMA = {soma:.2f}")
media = soma / n
print(f"MEDIA = {media:.2f}")
