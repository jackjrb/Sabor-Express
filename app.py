import os

restaurants = ['Pizza', 'Sushi']

def show_program_name():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def show_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finish_app():
    show_subtitle('Finalizando app\n')

def return_menu():
    input('Digite uma tecla para voltar ao menu principal: \n')
    main()

def show_subtitle(text):
    os.system('clear')
    #os.system('cli') windowns
    print(text)

def invalid_option():
    print('Opção inválida\n')
    return_menu()

def create_new_restaurant():
    show_subtitle('Cadastro de novos restaurantes\n')
    restaurant_name = input('Digite o nome do restaurante que desaja cadastrar: ')
    restaurants.append(restaurant_name)
    print(f'O restaurante {restaurant_name} foi cadastrado com sucesso')
    return_menu()

def restaurant_list():
    show_subtitle('Listando os restaurantes\n')

    for restaurant in restaurants:
        print(f'.{restaurant}')

    return_menu()

def choice_option():
    try:
        selected_option = int(input('Escolha uma opção:'))
        print(f'Você escolheu {selected_option}')
        #selected_option_number = int(selected_option)


        if selected_option == 1:
            print('Cadastrar restaurante')
            create_new_restaurant()
        elif selected_option == 2:
            print('Listar restaurante')
            restaurant_list()
        elif selected_option == 3:
            print('Ativar restaurante')
        elif selected_option == 4:
            finish_app()
        else:
            invalid_option()
    except:
        invalid_option()

def main():
    os.system('clear')
    show_program_name()
    show_options()
    choice_option()

if __name__ == '__main__':
    main()
