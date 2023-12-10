print("Senha")
# Guarda simplesmente o valor da senha
Senha = 2002
#Pedir a entrada/senha
Tentativa = int(input("Digite a senha: "))
# Verifica-se a senha colocada pelo usuário é a senha correta, caso contrário, pedir a senha novamente
while Tentativa != Senha:
    print("Senha Invalida")
    Tentativa = int(input("Digite a senha: "))
# Caso-se a senha colocada pelo usuário for a senha correta pra finalizar o código
print("Acesso permitido")