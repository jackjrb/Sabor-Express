user = 'Jackeline'
password = '1234'

user_input = input('Digite o seu usuário:\n')
password_input = input('Digite a sua senha:\n')

if user == user_input and password==password_input:
    print('Login efetuado com sucesso')
else:
    print('Usuário ou senha invalido')