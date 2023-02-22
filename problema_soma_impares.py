print("Digite dois números: ")
x = int(input())
y = int(input())

troca = 0
if x > y:
    troca = x
    x = y
    y = troca

soma = 0
print(x)
print(y)
for i in range(x+1, y):
    if i % 2 != 0:
        soma += i

print(f"SOMA DOS IMPARES --> {soma}")