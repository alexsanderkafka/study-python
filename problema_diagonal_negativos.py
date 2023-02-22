n = int(input("Qual a ordem da matriz: "))
matriz = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Elemento [{i}, {j}]: "))

print("DIAGONAL PRINCIPAL: ")
for i in range(n):
    print(f"{matriz[i][i]} ", end="")
print()

cont_negativos = 0
for i in range(n):
    for j in range(n):
        if matriz[i][j] < 0:
            cont_negativos += 1
print(f"QUANTIDADE DE NEGATIVOS = {cont_negativos}")
