'''Faça um algoritmo que preencha uma

matriz 3 X 3 de inteiros e escreva:
– A matriz completa
– A soma dos números ímpares da matriz
– A soma dos números pares da matriz'''

def imprimeMatrizDicionarios(matriz, linhas, colunas):
    for l in range(linhas):
        for c in range(colunas):
            print("%5.2f"%matriz[(l, c)], end=" ")
        print() #enter

m = {}

linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))
for l in range(linhas):
    for c in range(colunas):
        elem = float(input(f"Digite o elemento da linha {l} coluna {c}: "))
        m[(l, c)] = elem

print("matriz: ")
imprimeMatrizDicionarios(m, linhas, colunas)

'''SAÍDA
matriz:
 1.00  2.00
 3.00  4.00'''