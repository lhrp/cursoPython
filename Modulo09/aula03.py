# Digamos que estamos analisando a meta de vendas de vários funcionaários de uma empresa. A meta de vendas em reais, deve ser alcançada diariamente.
# Temos uma lista com as vendas de todos os funcionários e quero calcular qual o % das pessoas que alcançaram a meta.

vendas = [1200, 340, 560, 1230, 5000, 610, 2350, 1200, 340, 560, 1230, 5000, 610, 2350, 1200, 340, 560, 1230, 5000, 610, 2350, 1200, 340, 560, 1230, 5000, 610, 2350, 1200, 340, 560, 1230, 5000, 610, 2350, 1200, 340, 560, 1230, 5000, 610, 2350]
meta = 1000 

# Solução 1
metasAlcancadas = 0
for venda in vendas:
    if venda >= meta:
        print(f'Meta alcançada com {venda} reais de venda')
        metasAlcancadas += 1

print(f'{metasAlcancadas} pessoas alcançaram a meta')
print(f'{metasAlcancadas / len(vendas) * 100}% das pessoas alcançaram a meta')
