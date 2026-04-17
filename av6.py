# 6. A série de Fibonacci é formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … 
# Escreva um algoritmo que gere a série de FIBONACCI até o N-ésimo termo, sendo este informado pelo usuário.

n = int(input('Quantos números irão aparecer na sequência de Fibonacci: '))
index = 1
fibo = [1, 1]

if(n == 1):
    fibo.pop(1)
elif(n == 0):
    fibo = []
else:
    while (len(fibo) < n):
        fibo.append(fibo[index]+fibo[index-1])
        index += 1
print(fibo)

# Fibonacci é uma sequência, em que o próximo número, é uma soma dos dois anteriores a ele, então, utilizamos um index, começando na segunda posição,
# para poder pegar os valores que vão ser somados, enquanto a lista não for do tamanho requisitado pelo usuário, será adicionado a lista o valor na posição index somado com o valor
# na posição index anterior a ele, e também o index vai aumentar, falando pro sistema
# que a gente quer utilizar como próximo valor o número que foi adicionado.