###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Noite de Sono
###################################################

# Leitura de dados
print("Calculando o período de sono.")
print("Por favor, coloque as horas no modelo brasileiro, ou seja, oito horas da noite são 20 horas.")
print("Estamos levando em consideração de que você dormiu no período da noite e acordou no período da manhã.")
h_1 = int(input("Digite a hora em que você foi dormir: "))
m_1 = int(input("Digite o minuto em que você foi dormir: "))
h_2 = int(input("Digite a hota em que você acordou: "))
m_2 = int(input("Digite o minuto em que você acordou: "))

# Cálculo do tempo dormido
m_t = (60 - m_1) + m_2
h_t = (23 - h_1) + h_2
if (m_t >= 60):
    h_t = h_t + 1
    m_t = m_t - 60

# Impressão da resposta
if (m_t > 0):
    print("Você dormiu", h_t, "horas e", m_t, "minutos de sono!")
else:
    print("Você dormiu", h_t, "horas e", m_t, "minuto de sono!")
#print(h_t >= 8)
