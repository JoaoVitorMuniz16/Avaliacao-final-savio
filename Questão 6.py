# Variavel com a denominação media e outra varivel com a denominação quatidade:
media =0 
quantidade = 0
# Ele repete uma ação 6 vezes:
for i in range(6):
    # Pedir para o usúario colocar o valor  para ser armazenado em na variável "num"
    num = float(input(f'Digite o {i+1}° número: '))
    # Nesta parte o programa pegarar a media e somarar ao num
    if num > 0:
     media = media + num
     # Se o num for maior que 0 adicionar 1 na variável positivo
     quantidade = quantidade + 1

# Mostra-se quantidade de valores positivos
print(f"{quantidade} valores positivos")
# Mostra-se média da lista "numeros"
print(f"{media/quantidade :0.1f}")