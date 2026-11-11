import random

print("=🎥=CINEMA=🍿=")

while True:
    print("1 - Vingadores: Doutor Destino | 2h45")
    print("2 - Os Farofeiros 3 | 1h42")
    print("3 - O Gatola Da Cartola | 1h31")
    filme = int(input("Escolha um filme: "))
    
    print("--------------------------") #sessão
    
    if filme == 1:
        print("Sessão do filme 'Vingadores: Doutor Destino' às 20:00")
        print("Sessão de Segunda a Domingo")
        semana = input("Escolha o dia da semana: ")
        
        print("--------------------------") #quantidade
        
        ingressoTotal = 20
        ingresso1 = int(input("Quantidades de ingressos: "))
        if ingresso1 > 0 and ingresso1 <= 20:
            ingressoTotal -= ingresso1
            
        print("--------------------------") #cadeira
        
        print("Escolha seu Assento(escolha uma opção disponivel): ")
        print("A1 | A2 | A3 | A4 | A5")
        print("B1 | B2 | B3 | B4 | B5")
        print("C1 | C2 | C3 | C4 | C5")
        print("D1 | D2 | D3 | D4 | D5")
        print("E1 | E2 | E3 | E4 | E5")
        cadeira = input("Selecione sua(s) cadeira(s): ")
        
        print("--------------------------") #ingresso meia ou inteira
        
        print("Tabela de preços")
        print("inteira: R$30,00")
        print("meia: R$15,00")
        entrada = input("Tipo de ingresso: ")
        
        print("--------------------------") #pagamento
        
        print("1- Pix")
        print("2- Cartão")
        pagamento = int(input("Escolha o tipo de pagamento: "))
        if pagamento == 1:
            nome = input("Digite seu nome: ") 
            print("Código pix: jwu7dgt39elk2y9876r")
                        
        elif pagamento == 2:
            nome = input("Digite seu nome: ") 
            codigoCartao = int(input("Digite o código do cartão: "))
            cvv = int(input("Digite o CVV: "))
        else:
            print("Não é uma opção")
            
        print("--------------------------") #ingresso
        
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        sorteio = random.choice(numeros)
        
        print("🎟️INGRESSO🎟️")
        print(f"{nome}")
        print("Vingadores: Doutor Destino | 165 minutos")
        print(f"Cadeira:{cadeira} | Nº: {sorteio}")
        break
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    elif filme == 2:
        ingresso2 = int(input("Quantidades de ingressos: "))
        if ingresso2 > 0 and ingresso2 <= 20:
            totalSeçao2 -= ingresso2
            print(f"Compra realizada com sucesso! Quantidade disponivel de ingressos para o filme 'Os Farofeiros 3': {totalSeçao2} unidades")
        else:
            print("Ingressos esgotados")
            
    elif filme == 3:
        ingresso3 = int(input("Quantidades de ingressos: "))
        if ingresso3 > 0 and ingresso3 <= 20:
            totalSeçao3 -= ingresso3
            print(f"Compra realizada com sucesso! Quantidade disponivel de ingressos para o filme 'O Gatola Da Cartola': {totalSeçao3} unidades")
        else:
            print("Ingressos esgotados")
    else:
        ("Não é uma opção!")
