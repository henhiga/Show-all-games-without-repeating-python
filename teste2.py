final_arquivo = False
string_vazia = ''
lista=[]

meu_arquivo = open('times.txt', 'r')
#adiciona times para lista
while not final_arquivo:
    linha = meu_arquivo.readline()
    if linha == string_vazia:
        final_arquivo = True
    else:
        time = linha.rstrip()
        lista.append(time)
        

meu_arquivo.close()
#fixtures
n=len(lista)
teste=1
for i in range(n):
    for x in range(teste,n):
        print(lista[i], " X ",lista[x])
    teste+=1
    
    
