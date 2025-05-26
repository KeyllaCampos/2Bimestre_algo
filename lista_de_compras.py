
compras = []
opcao=input("deseja adicionar algum item na lista? ")

while opcao=="sim":
    adicionar=input("quais itens deseja adicionar? por favor adicione um por vez ")
    compras.append(adicionar)
    print(compras)
    opcao=input("deseja continuar?")

item_remover=input("deseja remover algum item?")
if item_remover =="sim":
    item_remover = input("Digite o nome do item que deseja remover: ")
    item_remover in compras
    compras.remove(item_remover)
    print(f"'{item_remover}' foi removido da lista.")

else:
    print(f"'{item_remover}' não está na lista.")

organizar=input("deseja organizar sua lista? ")

if organizar=="sim":
    compras.sort
    for item in compras:
        print("-", item)

elif organizar=="nao":
    print(compras)




