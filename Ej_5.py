nombre = input('¿Cuál es su nombre? ')
sexo = input('¿Y cuál es su sexo (hombre o mujer? ')
if sexo == 'hombre':
    if nombre.lower() > 'n':
        print('Perteneces a la casa de Gryffindor')
    else:
        print('Perteneces a la casa de Slytherin')
else:
    if nombre.lower() < 'm':
        print('Perteneces a la casa de Gryffindor')
    else:
        print('Perteneces a la casa de Slytherin')
