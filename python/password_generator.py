import random

#lista de caracteres que podem ser usados na senha
list_of_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

#tamanho da senha
length = int(input("Digite o número de caracteres para a senha: "))

#função que usa o length para gerar a senha
def generate_password(length):

    for i in range(length):
        password = ''.join(random.sample(list_of_characters, length))
                       
    return password

print(generate_password(length))