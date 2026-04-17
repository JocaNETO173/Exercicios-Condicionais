## Printa no terminal explicando o programa
print("Calculador de média aritmética de notas \n diga 4 de suas notas e a partir delas avaliarei a partir da média se você está ou não aprovado")
print("Digite no padrão '0,0', exemplo: nota 4,5")

## Variável com valor booleano para a condição do while
valorescorretos = False

## While responsável pela repetição dos inputs das notas enquanto 'valorescorretos' possuir valor falso
while(valorescorretos == False):
    ## Inputs responsáveis por receber as notas
    nota1 = float(input("Valor da primeira nota: ").replace(",", "."))
    nota2 = float(input("Valor da segunda nota: ").replace(",", "."))
    nota3 = float(input("Valor da terceira nota: ").replace(",", "."))
    nota4 = float(input("Valor da quarta nota: ").replace(",", "."))
    
    ## If resposável por analisar se as notas são válidas para a análise
    if(nota1 > 10.0 or nota1 < 0 or nota2 > 10.0 or nota2 < 0 or nota3 > 10.0 or nota3 < 0 or nota4 > 10.0 or nota4 < 0):
        print("Valor incorreto!")
    else:
        valorescorretos = True

## Variável responsável por calcular a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

## If que analisa se o usuário está aprovado e reprovado
if(media >= 6.0):
    print("aprovado")
else:
    print("reprovado")
## Printa no terminal qual é a média do usuário baseado nas notas ditas
print(f"sua média é {media}")