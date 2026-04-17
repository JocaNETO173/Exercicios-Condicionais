# 5. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
# Dada a massa inicial em gramas informada pelo usuário, 
# fazer um programa que calcula o tempo necessário para que essa massa se torne menor que 0,5 grama. 
# O programa deve escrever a massa inicial, a massa final e o tempo calculado em horas, minutos e segundos.

massaI = float(input('Massa inicial em gramas: ')) # o tipo float foi aplicado para que o tipo da varíavel fosse igual ao valor de 
# referência que a gente tem que é 0,5
massaF = massaI
seg = 0
min = 0
hour = 0

# Lógica usada pra poder calcular o tempo de cada loop, a cada fim de loop vai adicionar os 50 segundos, permitindo que possamos supor quanto tempo
# levou para o material atingir a massa menor que 0,5 gramas.
# Sempre que o valor de segundos passar de 60, vai adicionar 1 minuto, e sempre que minuto passar de 60, vai adicionar 1 hora
while (massaF >= 0.5):
    massaF /= 2
    seg += 50

if(seg >= 60):
    while (seg >= 60):
        min += 1
        seg -= 60
    if(min >= 60):
        while(min >= 60):
            hour += 1
            min -= 60


print(f'Massa Inicial = {massaI} .')
print(f'Massa Final = {massaF} .')
print(f'E a massa se tornou menor que 0.5 gramas em {hour} horas, {min} minutos e {seg} segundos.')

