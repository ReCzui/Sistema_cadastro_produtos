print('_-'*20)
print('   SISTEMA DE CADASTRO DE PRODUTOS   ')
print('_-'*20)


lista_produtos = []

while True:
    produto = {}
    produto['nome'] = input('Produto: ')
    produto['preço'] = float(input('Preço unitário: R$ '))
    produto['quantidade'] = int(input('Quantidade: '))
    produto['total'] = produto['preço'] * produto['quantidade']

    lista_produtos.append(produto)


    continua = input('Continuar? [S/N] ').upper().split()[0]
    if continua in 'N':
        break
print()
total_itens = 0
for item in lista_produtos:
    print(f'{item["nome"]}: \n R${item["preço"]:.2f}\n Quantidade: {item["quantidade"]}\n Total: R$ {item["total"]:.2f}')
    print()
    total_itens += item['total']

print('_-'*20)
print(f'  Valor total em estoque: {total_itens:.2f}  ')
print('_-'*20)

