def media_aluno():
    nota1 = int(input('Nota 1ª prova: '))
    nota2 = int(input('Nota 2ª prova: '))
    nota3 = int(input('Nota 3ª prova: '))

    soma_notas = nota1 + nota2 + nota3
    media_notas = soma_notas/3

    print(f'Média do aluno é {media_notas}')


media_aluno()
