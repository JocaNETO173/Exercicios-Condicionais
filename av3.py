## Print instruindo o usuário a o que fazer
print("Me diga dois numeros e qual ação deseja realizar")

## Duas variáveis resposáveis por receber o valor dos dois número desejados pelo usuário
n1 = float(input("Primeiro número: ").replace(",", "."))
n2 = float(input("Segundo número: ").replace(",", "."))

## Outro print demonstrando o menu de opções que o usuário pode realizar a partir do código
print("Quar ação deseja realizar?\n1- Soma de 2 números.\n2- Diferença entre 2 números \n3- Produto entre 2 números\n4- Divisão entre 2 números (o denominador não pode ser zero)")

## Variável com input recebendo qual é a ação desejada pelo usuário dependendo do número escolhido
acao = int(input("Ação desejada: "))

## If e elif utilizado para analisar qual foi a ação escolhida e realizá-la com base nos dois número escolhidos
if(acao == 1):
    print("Certo, irei realizar a soma dos números")
    resultado = n1 + n2
    print(f"A soma de {n1} e {n2} é igual a {resultado}")

elif(acao == 2):
    print("Certo, verificar a diferença de valor entre os números")
    if(n1 > n2):
        resultado = n1 - n2
    else:
        resultado = n2 - n1
    print(f"O valor da diferença entre {n1} e {n2} números é igual a {resultado}")

elif(acao == 3):
    print("Certo, irei analisar o produto dos dois números")
    resultado = n1 * n2
    print(f"O produto de {n1} e {n2} é igual a {resultado}")

elif(acao == 4):
    ## Dois whiles, um responsável por ver se o número 1 é 0 e caso seja devolve o input para que seja digitado outro número, caso o número 2 seja 0 seja digitado outro denominador, caso nenhum dos dois aconteça, a divisão ocorre normalmente.
    while(n1 == 0):
        print("Não é possível dividir 0, digite um novo número para ser dividido")
        n1 = float(input("Novo denominador: ").replace(",", "."))        
    while(n2 == 0):
        print("Não é possível dividir por 0, digite um novo denominador")
        n2 = float(input("Novo denominador: ").replace(",", "."))
    print("Certo, irei fazer a divisão dos valores")
    resultado = n1 / n2
    print(f"O resultado da divisão entre {n1} e {n2} é igual a {resultado}")
