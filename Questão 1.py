print("Saiba quanto de impostos você precisa pagar, Digite Abaixo")
#Pedir a entrada/salário
Salario = float(input("Digite seu salário: "))
#Se o valor for menor que 0 pedir que o usuário digite a entrada/salário novamente
while Salario < 0:
    print("\nDigite um salário válido.")
    Salario = float(input("Digite seu salário: "))
#Verificar-se o valor está entre 0R$ e 2000R$
if Salario <= 2000:
    print('Insento')
#Verificar-se o valor está entre 2000R$ e 3000R$.
elif Salario > 2000 and Salario < 3000.01: 
    print(f"R$ {Salario*(8/100):.2f}")
#Verificar-se o valor está entre 3000R$ e 4500R$
elif Salario > 3000 and Salario < 4500.01:
    print(f"R$ {Salario*(18/100):.2f}")
#Verificar-se o valor é maior que 4500R$
else:
    print(f"R$ {Salario*(28/100):.2f}")