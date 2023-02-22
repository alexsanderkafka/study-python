n = int(input("Quantos números você vai digitar: "))
vet = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um número: "))

print()
print("NÚMEROS DIGITADOS: ")
for i in range(0, n):
    print(vet[i])
