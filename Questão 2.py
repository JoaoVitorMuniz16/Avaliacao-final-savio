print("Descubre o valor do seu aumento. Digite Abaixo")
#Pedir a entrada/salário
Salario = float(input("Qual seu salário atual: "))
# Se o valor for menor que 0 pedir que o usuário digite a entrada/salário, novamente
while Salario < 0:
    print('\nDigite um valor válido!')
    Salario = float(input("Qual seu salário atual: "))
# se o valor está entre 0 e 400 e fazer as ações necessárias.
if Salario <= 400:
    print(f"Novo salário: {Salario+(Salario*(15/100)):.2f} \nReajuste ganho: {Salario*(15/100):.2f} \nEm percentual: 15 %")
# se o valor está entre 400R$ e 800R$ e fazer as ações necessárias.
elif Salario > 400 and Salario <= 800:
    print(f"Novo salário: {Salario+(Salario*(12/100)):.2f} \nReajuste ganho: {Salario*(12/100):.2f} \nEm percentual: 12 %")
# se o valor está entre 800R$ e 1200R$ e fazer as ações necessárias.
elif Salario > 800 and Salario <= 1200:
    print(f"Novo salário: {Salario+(Salario*(10/100)):.2f} \nReajuste ganho: {Salario*(10/100):.2f} \nEm percentual: 10 %")
#Verificar se o valor está entre 1200R$ e 2000R$ e fazer as ações necessárias.
elif Salario > 1200 and Salario <= 2000:
    print(f"Novo salário: {Salario+(Salario*(7/100)):.2f} \nReajuste ganho: {Salario*(7/100):.2f} \nEm percentual: 7 %")
#Verificar se o valor é maior do que 2000 e fazer as ações necessárias.
else:
    print(f"Novo salário: {Salario+(Salario*(4/100)):.2f} \nReajuste ganho: {Salario*(4/100):.2f} \nEm percentual: 4 %")