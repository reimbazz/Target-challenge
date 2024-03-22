numero = int(input("Informe um número para calcular sequência Fibonacci: "))
#variaveis para gravar a posição 1 e 0 durante o loop futuro
anterior = 0
proximo = 1

while proximo < numero:
    aux = proximo
    proximo += anterior
    anterior = aux

#compara-se o numero com o anterior caso o numero seja 0
if proximo == numero or proximo == anterior:
    print("O número pertence a sequência Fibonacci!!!")
else:
    print("O número não pertence a sequência de Fibonacci :(")
