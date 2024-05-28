import os

numbers=[]
names=[]
years=[]


def number_list():
    number = 0
    for number in range(1,11):
        number = int(len(numbers))+1
        numbers.append(number)
    print(f'{numbers}')
    sum_odd_numbers()
    descending_numbers()

def names_list():
    for count in range(0,4):
        name = input('Digite um nome: \n')
        names.append(name)
    print(f'{names}')

def years_list():
    actual = '2024'
    birth_year = input('Digite o ano que você nasceu\n')
    years.append(actual)
    years.append(birth_year)
    print(f'{years}')

def sum_odd_numbers():
    sum = 0
    for number in numbers:
        if(number%2!=0):
            sum+=number
    print(f'A soma dos números impares é: {sum}')

def descending_numbers():
    for count in range(len(numbers)-1, -1, -1):
        print(f'{numbers[count]}')

def multiplication_table():
    number = int(input('Digite um mnúmero que você queira saber a tabuada'))
    for count in range(1,11):
        multiplication = number * count
        print(f'{number} x {count} = {multiplication}')

def menu():
    print('1. Lista de numeros\n')
    print('2. Lista de nomes\n')
    print('3. Lista de ano\n')
    print('4. Tabuada')

    menu_number = int(input('Digite o numero do menu que deseja \n'))

    if(menu_number == 1):
        print('Lista de numeros')
        number_list()
    elif(menu_number==2):
        print('Lista de nomes')
        names_list()
    elif(menu_number==3):
        print('Lista de ano')
        years_list()
    elif (menu_number==4):
        print('Tabuada')
        multiplication_table()
    else:
        print('Tente novamente')
        main()

def main():
    os.system('clear')
    menu()

if __name__ == '__main__':
    main()
