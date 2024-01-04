# Fazer um programa que leia o nome de 5 produtos e a quantidade produzida de cada um deles.
# Ao final, o programa deve listar o nome e a quantidade produzida dos produtos.

produtos = ['coca', 'pepsi', 'guarana', 'fanta', 'sukita']
producao = [15000, 12000, 10000, 8000, 5000]

for i in range(5):
    print('Indice: ', i)
    print(produtos[i], producao[i])