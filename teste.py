## Foi criada uma variável para a condição do primeiro while
SequenciaValida = False

while(SequenciaValida == False):
    ## Também foi criada duas variáveis, o index para 'varrer' o input inserido pelo usuário e a 'sequencia' para guardar a sequência desejada pelo usuário
    index = 0
    sequencia = input("Sequencia: ").upper()
    ## While utilizado para passar durante toda a sequência, se uma letra não for um nucleotídeo, printa no terminal que a sequencia é válida e para este while, caso a última letra for um nucleotídeo então a variável 'SequenciaValida' é True e para o primeiro while
    while(index < len(sequencia)):
        if(sequencia[index] not in ['A', 'C', 'G', 'T']):
            print("Sequência inválida!")
            break
        elif(sequencia[len(sequencia) - 1] in ['A', 'C', 'G', 'T']):
            SequenciaValida = True
        index += 1

## Reinicia o valor do index
index = 0

## Foi feito um while para passar durante toda a sequencia, letra por letra, e compara para ver qual núcleotídeo atual, printa a posição (valor atual do index) e qual é o nucleotídeo
while(index < len(sequencia)):
    if(sequencia[index] == 'A'):
        print(f'{index+1} - {sequencia[index]}: Adenina')
    elif(sequencia[index] == 'C'):
        print(f'{index+1} - {sequencia[index]}: Citosina')
    elif(sequencia[index] == 'G'):
        print(f'{index+1} - {sequencia[index]}: Guanina')
    elif(sequencia[index] == 'T'):
        print(f'{index+1} - {sequencia[index]}: Timina')  
    index += 1