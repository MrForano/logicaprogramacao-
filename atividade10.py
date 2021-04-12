def odd_multiples_5():
    n = int(input("Insira um numero: "))

    for n in range(int(n)):
        if n % 5 == 0 and n % 2 != 0:
            print(n)


odd_multiples_5()


def user_list():
  entries = int(input("Digite quantidade de itens na lista: "))
  list = []
  i = 0
  while i < entries:
    list.append(input("Numeros a inserir na lista: "))
    i += 1
  return list


print(user_list())


def numbers_of_number(list):
    number_5 = 0
    for number in list:
        if number > 5:
            number_5 += 1
    return number_5


list = []
print(numbers_of_number(list))


def psg_x_bayern():
    choice = input("Escolha uma opção (a, b ou c): ")
    while choice != 'c':
        if choice == 'a':
            print("PSG")
        elif choice == 'b':
            print("BAYERN")
        choice = input()


print(psg_x_bayern())
