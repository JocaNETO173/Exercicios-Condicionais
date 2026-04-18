## Print no console que demonstra o que o código faz
print("Verificador de complementar de um caractere de nucleotídeo")

## Variável com input responsável por receber o nucleotídeo desejado pelo usuário
nucleotideo = input("Digite um caractere de nuclotídeo (A, G, C, T): ").upper()

## if, elif e else que comparam qual é o nucleotídeo junto com qual é o complementar, e se não for nenhum devolve "Nucleotídeo Inválido!" no terminal
if(nucleotideo == "A"):
    NucleotideoEspecificado = "A (Adenina)"
    complementar = "T (Timina)"
elif(nucleotideo == "G"):
    NucleotideoEspecificado = "G (Guanina)"
    complementar = "C (Citosina)"
elif(nucleotideo == "C"):
    NucleotideoEspecificado = "C (Citosina)"
    complementar = "G (Guanina)"
elif(nucleotideo == "T"):
    NucleotideoEspecificado = "T (Timina)"
    complementar = "A (Adenina)"
else:
    print("Nucleotídeo inválido!")

## If responsável por printar qual é o nucleotídeo e complementar a partir do nucleotídeo digitado pelo usuário
if(nucleotideo in ["A", "G", "C", "T"]):
    print(f"O complementar de {NucleotideoEspecificado} é {complementar}")
