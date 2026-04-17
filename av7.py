## Printa no terminal a explicação do programa.
print('Digite número inteiros e positivos, e após direi qual é o maior e o menor dito\nPara encerrar a entrada de dados digite 0')

## Foi criado um array para que seja adicionado os números que o usuário inserir e uma variável com valor booleano para a condição do primeiro while.
ArrayNumeros = []
RespostaValida = False

while(RespostaValida == False):
    ## Input do número desejado pelo usuário.
    numero = int(input("Digite um número: "))

    ## Checa se não é um input vazio e se o número é positivo, se sim acrescenta o número no array, se não, printa uma mensagem dizendo que não é um valor válido e devolve para que o usuário escreva outro número.
    if(numero == "" or numero < 0  ):
        print("Valor inválido, não será utilizado na avaliação!")
    elif(numero > 0):
        ArrayNumeros.append(numero)
    
    ## Checa se o input é 0, se sim e o array possuir pelo menos dois números inseridos para o loop, se não tiver pelo menos dois números printa uma mensagem avisando e devolve para que o usuário escreva mais números.
    if(numero == 0 and len(ArrayNumeros) > 1):
        RespostaValida = True
    elif(numero == 0 and len(ArrayNumeros) < 2):
        print("Não é possível a avaliação com menos de 2 números")

## Criamos 3 variáveis, um resposável pelo número maior, outro para o menor, e o index para que seja possível passar por toda a lista.
NumeroMaior = 0
NumeroMenor = ArrayNumeros[0]
index = 0

## Enquanto index for menor que o comprimento do array o while se repetirá
while(index < len(ArrayNumeros)):
    ## Se o número que está sendo analisado for menor que o valor da variável "NumeroMenor" substitui o valor da variável pelo número que foi analisado, se não, continua o código.
    if(ArrayNumeros[index] < NumeroMenor):
        NumeroMenor = ArrayNumeros[index]
    ## Se o número que está sendo avaliado for maior que o valor da variável "NumeroMaior" substitui o valor da variável pelo número que foi analisado, se não, continua o código.
    if(ArrayNumeros[index] > NumeroMaior):
        NumeroMaior = ArrayNumeros[index]
    ## Adiciona 1 no na variável "index"
    index += 1

## Printa no terminal o resultado final da análise.
print(f"Dos números passados, o menor número é {NumeroMenor} e o maior número é {NumeroMaior}")