hora = int(input("Digite uma hora do dia: "))

if hora < 12:
    print("Bom dia")
elif hora < 18:
    print("Boa tarde")
else:
    print("Boa noite")

soma = 0
x = int(input("Digite o primeiro numero: "))
while x != 0:
    soma += x
    x = int(input("Digite outro numero: "))
    
print(f"SOMA 1 --> {soma}")
print()

soma2 = 0
n = int(input("Quantos numeros serao digitados: "))
for i in range(0, n):
    x2 = int(input("Digite um numero: "))
    soma2 += x2

print(f"SOMA 2 --> {soma2}")
print()

