#Venda Combo    
escolha = int(input("-----Boa Noite!!------\nO escolha opções:\n1 -> Hamburguer - custa R$ 10,00\n2 -> Batata Frita - custa R$ 10,00\n3 -> Refrigerante - custa R$ 10,00\n4 -> Combo - R$22.00\n"))

Item1 = "hamburguer"
Item2 = "batata Frita"
Item3 = "Refrigerante"
Item4 = "Combo"

#Hamburguer
if(escolha == 1):
    print(f"Você escolheu {Item1}")
    adicional = int(input("Gostaria de adicionar outro Item? \n2 -> Batata Frita - custa R$ 10,00\n3 -> Refrigerante - custa R$ 10,00\n"))
    if (adicional == 2):
        print(f"Você escolheu {Item1} e {Item2}")
        oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Item1} + {Item2} + {Item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Item1} + {Item2},  totalizando R$20,00")
    elif (adicional == 3):
        print(f"Você escolheu {Item1} e {Item3} \n")
        oferecercombo = input("Gostaria de adicionar o Batata Frita por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Item1} + {Item2} + {Item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Item1} + {Item3},  totalizando R$20,00")
    else:
        print(f"Seu pedido é {Item1},  totalizando R$10,00")

#Batata Frita
elif(escolha == 2):
    print(f"Você escolheu {Item2}")
    adicional = int(input("Gostaria de adicionar outro Item? \n1 -> Hamburguer - custa R$ 10,00\n2 -> Refrigerante - custa R$ 10,00\n"))
    if (adicional == 1):
        print(f"Você escolheu {Item1} e {Item2}")
        oferecercombo = input("Gostaria de adicionar o Batata Frita por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Item1} + {Item2} + {Item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Item1} + {Item3},  totalizando R$20,00")
    elif (adicional == 3):
        print(f"Você escolheu {Item2} e {Item3} \n")
        oferecercombo = input("Gostaria de adicionar o Hamburguer por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Item1} + {Item2} + {Item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Item2} + {Item3},  totalizando R$20,00")
    else:
        print(f"Seu pedido é {Item2},  totalizando R$10,00")

#Refrigerante
elif(escolha == 3):
    print(f"Você escolheu {Item3}")
    adicional = int(input("Gostaria de adicionar outro Item? \n2 -> Batata Frita - custa R$ 10,00\n3 -> Refrigerante - custa R$ 10,00\n"))
    if (adicional == 2):
        print(f"Você escolheu {Item1} e {Item2}")
        oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Item1} + {Item2} + {Item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Item1} + {Item2},  totalizando R$20,00")
    elif (adicional == 3):
        print(f"Você escolheu {Item1} e {Item3} \n")
        oferecercombo = input("Gostaria de adicionar o Batata Frita por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Item1} + {Item2} + {Item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Item1} + {Item3},  totalizando R$20,00")
    else:
        print(f"Seu pedido é {Item1},  totalizando R$10,00")