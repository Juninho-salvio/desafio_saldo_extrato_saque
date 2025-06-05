#lista menu, aparece sempre.
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
e1 = "EXTRATO"

#loop infinito
while True:

#Chamada para o MENU
    opcao = input(menu)

#Depositar
    if opcao == "1":
        print("------------------------------------------------------------------")
        print("                         DEPOSITAR:")
        print(" ")
        valor = float(input("Informe o valor do Depósito: R$ "))      
        print(" ")
        print("------------------------------------------------------------------")

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"    

        else:
            print("------------------------------------------------------------------")
            print("                         DEPOSITAR:")
            print(" ")
            print("                         ATENÇÃO.")
            print("                 Operação errada, valor invalido.")    
            print(" ")
            print("------------------------------------------------------------------")

#Sacar       
    elif opcao == "2":
        print("------------------------------------------------------------------")
        print("                               SACAR: ")
        print(" ")
        valor = float(input("Informe o valor do saque: R$ "))      
        print(" ")
        print("------------------------------------------------------------------")
       
       #Condicionais:
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("------------------------------------------------------------------")
            print("                               SACAR: ")
            print(" ")
            print("Operação falhou! Você não tem saldo suficiente.")     
            print(" ")
            print("------------------------------------------------------------------")
       
        elif excedeu_limite:
            print("------------------------------------------------------------------")
            print("                               SACAR: ")
            print(" ")
            print("Operação falhou! O valor do saque excede o limite.")     
            print(" ")
            print("------------------------------------------------------------------")
            
        elif excedeu_saques:
            print("------------------------------------------------------------------")
            print("                               SACAR: ")
            print(" ")
            print("Operação falhou! Número máximo de saques excedido.") 
            print(" ")
            print("------------------------------------------------------------------")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("------------------------------------------------------------------")
            print("                               SACAR: ")
            print(" ")
            print("Operação falhou! O valor informado é inválido.") 
            print(" ")
            print("------------------------------------------------------------------")

#Extrato              
    elif opcao == "3":
        print("------------------------------------------------------------------")
        print(e1.center(60," "))
        print(" ")
        print("Não foram realizadas movimentações." 
              if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(" ")
        print("------------------------------------------------------------------")

#Sair 
    elif opcao == "0":
        break

    else:
        print("------------------------------------------------------------------\n")
        print(" ")
        print("Operação inválida, por favor selecione novamente a operação desejada.")  
        print(" ")
        print("------------------------------------------------------------------")

        