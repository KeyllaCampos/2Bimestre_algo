#não pode ser alterada. garante a integridade dos dados
numero =(0, 8, 12, 8, 7, 8, 3)
#para ser uma tupla precisa estar entre parenteses
print("tupla original: ", numero)
#imprimindo para o usuario a tupla original, sem manipulações
print("tamanho da tupla: ", len(numero))
print("acessando pelo indice: ", numero[2])
#escolhendo qual item sera mostrado atraves do indice, lembrando que começa no 0
print("fazendo slicing do 2 ao 5: ", numero[2:5])
#o slicing ele não pega o ultimo item definido no recorte
print("quantas vezes o numero 8 repete: ", numero.count(8), "vezes")
print("posição da primeira ocorrencia do numero 7: ", numero.index(7))
minimo_tupla=min(numero)
print("menor numero dentro da tupla é: ", minimo_tupla)
maximo_tupla=max(numero)
print("maior numero dentro da tupla é: ", maximo_tupla)
print("soma dos numeros da tupla é: ", sum(numero))
tuplas_ordenadas=sorted(numero)
print("os numeros em ordem utilizando o metodo sorted", tuplas_ordenadas)
print("o numero 4 está na tupla?", 4 in numero)
numero2=(15,20)
tupla_concatenada=numero+numero2
print("a concatenação da tuplas 1 e 2 resulta na nova tupla: ", tupla_concatenada)
tupla_duplicada=numero * 2
print("tupla 1 duplicada: ", tupla_duplicada)