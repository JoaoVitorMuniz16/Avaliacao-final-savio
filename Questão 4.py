# Pedir para o usuario digitar o numero de telefone:
numero = int(input(f"Digite seu número de telefone do brasil \n Obs: Não utilize espaços e nem sinais:"))
# Os dois primeiros digitos do telefone serar salvo 
numero = int(str(numero)[:2])
# Os dois numeros que foram salvos serão comparados, e o programa identificarar o seu DDD
if numero == 61:
    print("Brasília")
elif numero == 71:
    print("Salvador")
elif numero == 11:
    print("São Paulo")
elif numero == 21:
    print("Rio de Janeiro")
elif numero == 32:
    print("Juiz de Fora")
elif numero == 19:
    print("Campinas")
elif numero == 27:
    print("Vitória")
elif numero == 31:
    print("Belo Horizonte")
else:
    print("Este ddd não esta registrado no sistema...") # Aparece caso o Usuario não Registrou o DDD certo