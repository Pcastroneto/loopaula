#armazena um numero pequeno

maior_numero = -999999999

# entra com o primmeiro numero
number = int(input('Entre com um número ou digite -1 para parar: '))

#Se o numero não for igual a -1 continua
while number != -1:
    #o numero é maior que o maior_numero
    if number > maior_numero:
    #sim, atualiza o maior numero.
         maior_numero = number
     #entre com o próximo numero.
    number = int(input('Entre com um número ou digite -1 para parar: '))
    
#Print o maior numero 
print('O Maior número é:', maior_numero)
    