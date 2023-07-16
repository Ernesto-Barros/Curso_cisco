minha_lista_ordenada=[]
tamanho_da_lista=int(input("digite o tamnho inicial da lista"))

for i in range(0,tamanho_da_lista):
    minha_lista_ordenada.append(int(input("Digite um numero ")))
    minha_lista_ordenada.sort()

print(' A lista ordenada é',minha_lista_ordenada)

for i in minha_lista_ordenada:
    if i % 2 != 0:
       print(i)
print(minha_lista_ordenada)