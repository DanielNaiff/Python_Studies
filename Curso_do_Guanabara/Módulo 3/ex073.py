times = (
    "Atlético-MG", "Bahia", "Botafogo", "Red Bull Bragantino", "Ceará", "Corinthians", "Cruzeiro",
    "Flamengo", "Fluminense", "Fortaleza", "Grêmio", "Internacional", "Juventude", "Mirassol",
    "Palmeiras", "Santos", "São Paulo", "Sport", "Vasco", "Vitória"
)

print('-=' * 15)
print(f'Lista de time do brasileirao: {times}')
print('-=' * 15)
print(f'Lista dos 5 primeiros times: {times[0:5]}')
print('-=' * 15)
print(f'Lista dos 4 ultimos times: {times[-4:]}')
print('-=' * 15)
print(f'Times ordenados: {sorted(times)}')
print('-=' * 15)
print(f'Bahia esta: {times.index("Bahia") + 1} posicao')