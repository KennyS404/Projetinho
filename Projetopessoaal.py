import time 
import os
import random
randomm = random.randrange(100000)
def animate_text(text):
  Kenny=1
  while Kenny:
    print("\n")
    print(text[0:Kenny])
    Kenny += 1
    if Kenny > len(text):
      Kenny = 0
    time.sleep(0.15)
    os.system('clear')  
animate_text("Seja bem vindo!!! \nComeçando programa....")

listabrinquedos = []
listabrinquedos1 = []
listabrinquedos2 = []
cont1 = 0
cont = 0
gg = 1234
cont2 = 0
soma = 0
soma1 = 0
soma2 = 0
atual = 0
total = 0
sales1 = 0
sales2 = 0
sales3 = 0
abertura_de_caixa = 0
saving = 0
import os
import time
def lin():
    print("*****pass*",randomm,"*word*******")
    senha = int(input("Digite a senha do caixa \n*************************** \nAqui: "))
    
    if senha !=randomm:
        animate_text("Acesso negado...")
        return lin()
    else:
        animate_text("Acesso liberado...")
        pass
    print("****************")
    nome1 = input("Nome do operador: \n**************** \nAqui: ")
    print("#NOTA",nome1,"o caixa deve ser iniciado com zero, pois é seu primeiro dia de trabalho \n")
    abertura_de_caixa = int(input("Digite o valor do dia anterior: \n"))
    if abertura_de_caixa != saving:
        print("Rapaz, isso aí é roubo de caixa, hoje é seu primeiro dia")
    elif total == 0:
        pass
lin()

while 'option' != 0:

    menu = int(input(
        "Selecione as opções \n #NOTA Os brinquedos selecionados na opção [1] devem ser selecionados na opção [3] para evitar justa causa por desatenção \n [1] Iniciar locação \n [2] Finalizar locação \n [3] Venda de produtos \n [4] Fechar caixa \n [5] Sair \n "))

    # condicãodasopçõesmenu1
    if menu == 1:
        brinquedo = int(input("Escolha o brinquedo para locação \n [0] Urso \n [1] Carro \n [2] Caminhão \n "))
        # Tratamento pra não perder ponto
        if brinquedo < 0 or brinquedo > 2:
            print("OPÇÃO INVÁLIDA, SELECIONE DE 0 A 2")
        
        if brinquedo == 0:
            brinquedo = 'Urso'
            cont = cont + 1
            soma = cont * 25
            # flag cont
            if cont > 3:
                print("Apenas 3 brinquedos simultaneos")
                cont = cont - 1
            if cont == 3 or cont < 3:
                print(3 - cont, brinquedo, "liberados")
            # adicionar no indice
            listabrinquedos.append(brinquedo)
            print(listabrinquedos, cont, "/ 3 BRINCANDO")

        # flag repetição lista brinquedos
        if brinquedo in listabrinquedos:
            listabrinquedos.remove(brinquedo)

        if brinquedo == 1:
            brinquedo = 'Carros'
            cont1 = cont1 + 1
            soma1 = cont1 * 30
            # flag cont
            if cont1 == 3:
                print("Todos os", brinquedo, "estão ocupados")
            if cont1 > 3:
                print("Apenas 3 brinquedos simultaneos")
                cont1 = cont1 - 1
            if cont1 == 3 or cont1 < 3:
                print(3 - cont1, brinquedo, "liberados")
                # adicionar no indice
            listabrinquedos1.append(brinquedo)
            print(listabrinquedos1, cont1, "/ 3 BRINCANDO")

        # flag repetição listabrinquedos
        if brinquedo in listabrinquedos1:
            listabrinquedos1.remove(brinquedo)

        if brinquedo == 2:
            brinquedo = 'Caminhão ou 4x4'
            cont2 = cont2 + 1
            soma2 = cont2 * 35
            # flag cont
            if cont2 > 3:
                print("Apenas 3 brinquedos simultaneos")
                cont2 = cont2 - 1
                # liberados
            if cont2 == 3 or cont2 < 3:
                print(3 - cont2, brinquedo, "liberados")
            # adicionar no indice
            listabrinquedos2.append(brinquedo)
            print(listabrinquedos2, cont2, "/ 3 BRINCANDO")

        # flag repetição listabrinquedos
        if brinquedo in listabrinquedos2:
            listabrinquedos2.remove(brinquedo)
            
    
    if menu == 2:
        stop = int(input("Entre com o brinquedo para parar a brincadeira:\n [0] Urso \n [1] Carro \n [2] Caminhão \n "))
        if stop > 2 or stop < 0:
            print("Por favor, selecione um valor válido")
        if cont == 0:
            print("Cara, o brinquedo já está livre")
        if cont1 == 0:
            print("Cara, o brinquedo já está livre")
        if cont1 == 0:
            print("Cara, o brinquedo já está livre")
        elif stop == 0:
            cont = cont - 1
            print("O brinquedo urso foi liberado")
        elif stop == 1:
            cont1 = cont1 - 1
            print("O brinquedo carro foi liberado")
        elif stop == 2:
            cont2 = cont2 - 1
            print("O brinquedo caminhão foi liberado")
       
    time.sleep(1.9)
    os.system('clear')
    if menu == 3:
        sales = int(input("Entre com os produtos vendidos \n [1] Ursos \n [2] Carros \n [3] Caminhões: \n"))

        if sales == 1:
            print("Produto urso adicionado ao sistema \n")
            sales1 = 1
        elif sales == 2:
            print("Produto carro adicionado ao sistema \n")
            sales2 = 2
        elif sales == 3:
            print("Produto caminhão adicionado ao sistema \n")
            sales3 = 3
        else:
            print("Digite algo valido")

    if menu == 4:

        if sales1 == 1:
            urso1 = print("A soma dos ursos é de: {}R$ \n".format(soma))
        elif cont == 0:
            pass
        if sales1 !=1:
            soma = 0
            print("É necessário informar o produto comprado (Urso) na opção [3] ao menos uma vez para que o sistema reconheça \n")


        if sales2 == 2:
            carro = print ("A soma dos carros é de: {}R$ \n".format(soma1))
        elif cont1 == 0:
            pass
        if sales2 !=2:
            print("É necessário informar o produto comprado (Carro) na opção [3] ao menos uma vez para que o sistema reconheça \n")
            soma1 = 0

        if sales3 == 3:
            caminhão = print("A soma dos caminhões é de: {}R$ \n".format(soma2))
        elif cont2 == 0:
            pass
        if sales3 !=3:
            soma2 = 0
            print("É necessário informar o produto comprado (Caminhão) na opção [3] ao menos uma vez para que o sistema reconheça \n")

        total = soma + soma1 + soma2 + saving

        total2 = print("O total do caixa é: {}R$ \n".format(total))
        saving = total
        if saving !=0:
            #NOTA O saving precisa ter valor no dia seguinte para que o cálculo da porcentagem seja feito corretamente
            atual = soma + soma1 + soma2 - saving / (saving) * (100)

            print("O percentual dos produtos vendidos em comparação com o dia anterior é de: {}% \n".format(atual))
            

        soma1 = 0
        soma = 0
        soma2 = 0
        cont = 0
        atual = 0
        cont1 = 0
        cont2 = 0
        lin()
    if menu == 5:
        print("Foi bom enquanto durou......")
        break
time.sleep(1.9)
os.system('clear')


