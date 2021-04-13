def student_media():
    nota1 = int(input('Nota 1ª prova: '))
    nota2 = int(input('Nota 2ª prova: '))
    nota3 = int(input('Nota 3ª prova: '))

    plus_notes = nota1 + nota2 + nota3
    media_notes = plus_notes/3

    print(f'Média do aluno é {media_notes}')


student_media()


def exit_list():
  entries_numbers = int(input("Insira o tamanho da lista: "))
  exit_list = []
  i = 0
  while i < entries_numbers:
    exit_list.append(input("Insira os numeros da lista: "))
    i += 1
  return exit_list


print(exit_list())


def globo_x_sbt():
  entry = input("Digite 'a' para Globo, 'b' para SBT e 'z/Z' para finalizar: ")
  while entry != 'z' or entry != 'Z':
    if entry == 'a':
        print("Globo")
    elif entry == 'b':
        print("SBT")
    else:
        print("Inválido")
        break
    entry = input()

print(globo_x_sbt())


def professorcoxa(list):
  medias_menores_7 = 0
  for number in list:
    if number < 7:
      medias_menores_7 += 1
  if medias_menores_7 * len(list) > 0.25:
    return "Professor Coxa"
  else:
    return "Professor Padrão"


list = []
print(professorcoxa(list))
