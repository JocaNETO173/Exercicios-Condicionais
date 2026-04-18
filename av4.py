## Print demonstrando o que o código faz
print("Verificador de preço, analisarei a partir de seu sexo e idade")

## Variável para a condição do while
respostaValida = False

## While responsável por repetir o input perguntando qual o sexo do usuário até que seja válida
while(respostaValida == False):
    SEntrada = input("Qual seu sexo?(M- Masculino F- Feminino) Resposta: ").lower()
    if(SEntrada not in ["m","f"]):
        print("Resposta inválida!")
    else:
        respostaValida = True

## Variável resposável por armazenar a idade do usuário
idade = int(input("Qual sua idade? Resposta:"))

## If e elif responsável por analisar os inputs e assim printar a opção correta de preço
if(idade < 10 or idade >65):
    print("O valor da entrada é R$0,50")
elif(idade >= 10 and idade <= 17):
    print("O valor da entrada é R$4,28")
elif(SEntrada == "f" and idade >=18 and idade <=65):
    print("O valor da entrada é R$5,50")
elif(SEntrada == "m" and idade >=18 and idade <=65):
    print("O valor da entrada é R$8,25")