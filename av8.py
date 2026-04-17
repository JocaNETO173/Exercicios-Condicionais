# 8. Escreva um algoritmo que recebe uma sequência de DNA e que percorre essa sequência imprimindo, para cada posição, 
# qual é o nome do nucleotídeo da posição. Por exemplo: dada a sequência AGGTC, o seu algoritmo deve imprimir a seguinte saída:

# 1 – A: Adenina
# 2 – G: Guanina
# 3 – G: Guanina
# 4 – T: Timina
# 5 – C: Citosina

# Caso a sequência possua algum caractere diferente dos descritos acima, o seu algoritmo deve escrever: “Nucleotídeo inválido!”

print('Insira uma sequência de DNA\nAdenina (A), Citosina (C), Guanina (G) e Timina (T)\nExemplo: AGGCT')
sequencia = input('Insira sua sequência: ')
sequencia = sequencia.strip().upper()
index = 0


while(index < len(sequencia)):
    if(sequencia[index] == 'A'):
        print(f'{index+1} - {sequencia[index]}: Adenina')
    elif(sequencia[index] == 'C'):
        print(f'{index+1} - {sequencia[index]}: Citosina')
    elif(sequencia[index] == 'G'):
        print(f'{index+1} - {sequencia[index]}: Guanina')
    elif(sequencia[index] == 'T'):
        print(f'{index+1} - {sequencia[index]}: Timina')
    else:
        print('Nucleotídeo Inválido!')
        break

    index+=1

