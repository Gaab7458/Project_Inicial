#Descontos> Algoritimo que le um preço dá desconto e mostra o novo preço!
preco = float(input('Digite o valor da sua compra: R$'))
if preco >= 100:
    novo = preco - (preco*5/100)
    print('Sua compra de R${:.2f} é maior ou igual a R$100,00 e por isso com desconto de 5% vai sair por R${:.2f}'.format(preco,novo))
elif preco >= 50: 
    if preco < 100:
        novo2 = preco - (preco*2/100)
        print('Sua compra de R${:.2f} é maior do que R$50,00 e menor do que R$100,00 e por isso vai sair com desconto de 2% vai sair por R${:.2f}'.format(preco,novo2))
elif preco >= 20:
    if preco < 50:
            novo3 = preco - (preco*1/100)
            print('Sua compra de R${:.2f} é maior do que R$20,00 e menor do que R$50,00 e por isso tem desconto de 1% e vai sair por {:.2f}'.format(preco,novo3))