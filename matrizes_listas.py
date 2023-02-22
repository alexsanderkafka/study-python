li = int(input("Quantas linhas vai ter a matriz: "))
co = int(input("Quantas colunas vai ter a matriz: "))

mat = [[0 for x in range(co)] for o in range(li)]

for i in range(0, li):
    for j in range(0, co):
        mat[i][j] = int(input(f"Elemento [{i}, {j}]: "))

print()
print("MATRIZ DIGITADA: ")
for i in range(0, li):
    for j in range(0, co):
        print(f"{mat[i][j]} ", end="")
    print()
