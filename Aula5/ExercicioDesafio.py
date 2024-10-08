#Venda Combo    
escolha = int(input("-----Boa Noite!!------\nO escolha opções:\n1 -> Hamburguer - custa R$ 10,00\n2 -> Batata Frita - custa R$ 10,00\n3 -> Refrigerante - custa R$ 10,00\n4 -> Combo - R$22.00\n"))

Hamb_1 = "hamburguer"
BFrita_2 = "batata Frita"
Ref_3 = "Refrigerante"
Combo_4 = "Combo"

#Hamburguer
if(escolha == 1):
    print(f"Você escolheu {Hamb_1}")
    adicional = int(input("Gostaria de adicionar outro Item? \n2 -> Batata Frita - custa R$ 10,00\n3 -> Refrigerante - custa R$ 10,00\n"))
    if (adicional == 2):
        print(f"Você escolheu {Hamb_1} e {BFrita_2}")
        oferecercombo = input("Gostaria de adicionar o Refrigerente por mais R$2,00? (Sim ou Não)").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Hamb_1} + {BFrita_2} + {Ref_3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Hamb_1} + {BFrita_2},  totalizando R$20,00")
    elif (adicional == 3):
        print(f"Você escolheu {Hamb_1} e {Ref_3} \n")
        oferecercombo = input("Gostaria de adicionar o Batata Frita por mais R$2,00? (Sim ou Não)").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Hamb_1} + {BFrita_2} + {Ref_3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Hamb_1} + {Ref_3},  totalizando R$20,00")
    else:
        print(f"Seu pedido é {Hamb_1},  totalizando R$10,00")

#Batata Frita
elif(escolha == 2):
    print(f"Você escolheu {BFrita_2}")
    adicional = int(input("Gostaria de adicionar outro Item? \n1 -> Hamburguer - custa R$ 10,00\n3 -> Refrigerante - custa R$ 10,00\n"))
    if (adicional == 1):
        print(f"Você escolheu {Hamb_1} e {BFrita_2}")
        oferecercombo = input("Gostaria de adicionar o Refrigerante por mais R$2,00? (Sim ou Não)").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Hamb_1} + {BFrita_2} + {Ref_3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Hamb_1} + {BFrita_2},  totalizando R$20,00")
    elif (adicional == 3):
        print(f"Você escolheu {BFrita_2} e {Ref_3} \n")
        oferecercombo = input("Gostaria de adicionar o Hamburguer por mais R$2,00? (Sim ou Não)").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Hamb_1} + {BFrita_2} + {Ref_3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {BFrita_2} + {Ref_3},  totalizando R$20,00")
    else:
        print(f"Seu pedido é {BFrita_2},  totalizando R$10,00")

#Ref_3rigerante
elif(escolha == 3):
    print(f"Você escolheu {Ref_3}")
    adicional = int(input("Gostaria de adicionar outro Item? \n1 -> Hamburguer - custa R$ 10,00\n2 -> Batata Frita - custa R$ 10,00\n"))
    if (adicional == 2):
        print(f"Você escolheu {Ref_3} e {BFrita_2}")
        oferecercombo = input("Gostaria de adicionar o Hamburguer por mais R$2,00? (Sim ou Não)").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Hamb_1} + {BFrita_2} + {Ref_3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Ref_3} + {BFrita_2},  totalizando R$20,00")
    elif (adicional == 1):
        print(f"Você escolheu {Hamb_1} e {Ref_3} \n")
        oferecercombo = input("Gostaria de adicionar o Batata Frita por mais R$2,00? (Sim ou Não)3").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {Hamb_1} + {BFrita_2} + {Ref_3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {Hamb_1} + {Ref_3},  totalizando R$20,00")
    else:
        print(f"Seu pedido é {Ref_3},  totalizando R$10,00")
#Combo
elif(escolha == 4):
    print(f"Você escolheu {Combo_4}")
else:
    print("Numereção invalida, tente novamente!")