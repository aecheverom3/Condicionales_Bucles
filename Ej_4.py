edad = int(input('¿Cuál es tu edad? '))
ingresos = float(input('¿Y cuáles son tus ingresos? '))
if edad < 16 and ingresos < 1000:
    print('No tienes que tributar')
else:
    print('Tienes que tributar')
