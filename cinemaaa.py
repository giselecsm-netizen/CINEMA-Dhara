import random

print("=🎥=CINEMA=🍿=")

while True:
    print("1 - Vingadores: Doutor Destino | às 20:00")
    print("2 - Os Farofeiros 3 | às 16:00")
    print("3 - O Gatola Da Cartola | às 13:00")
    filme = int(input("Escolha um filme: "))
    
    print("--------------------------") #sessão
    
    if filme == 1:
        print("Sessão do filme 'Vingadores: Doutor Destino' às 20:00")
        print("Sessão de Segunda a Domingo")
        semana = input("Escolha o dia da semana: ")
        
        print("--------------------------") #quantidade
        
        ingressoTotal = int(input("Quantidades de ingressos: "))
        if ingressoTotal > 0 and ingressoTotal <= 20:
            print(f"Quantidade escolhida: {ingressoTotal}")
        else:
            print("Não é uma opção")
            entrada = input("Tipo de ingresso: ")
            
        print("--------------------------") #cadeira
        
        print("Escolha seu Assento(escolha uma opção disponivel): ")
        print("A1 | A2 | A3 | A4 | A5")
        print("B1 | B2 | B3 | B4 | B5")
        print("C1 | C2 | C3 | C4 | C5")
        print("D1 | D2 | D3 | D4 | D5")
        print("E1 | E2 | E3 | E4 | E5")
        if ingressoTotal != 1:
            cadeira = input("Selecione suas cadeiras: ")
        else:
            cadeira = input("Selecione sua cadeira: ")

        print("--------------------------") #ingresso meia ou inteira
        
        print("Tabela de preços")
        print("1- inteira: R$30,00")
        print("2- meia: R$15,00")
        entrada = int(input("Tipo de ingresso: "))
        if entrada == 1:
            entrada = 30
        elif entrada == 2:
            entrada = 15
        else:
            print("Não é uma opção")
            break
            entrada = input("Tipo de ingresso: ")
        
        print("--------------------------") #pagamento
        
        print("1- Pix")
        print("2- Cartão")
        pagamento = int(input("Escolha o tipo de pagamento: "))
        if pagamento == 1:
            nome = input("Digite seu nome: ") 
            pagamentoFinal = entrada * ingressoTotal
            print(f"Preço a pagar {pagamentoFinal}")
            print("Código pix: jwu#7dgt39el@k2y9876r")
              
        elif pagamento == 2:
            nome = input("Digite seu nome: ")  
            pagamentoFinal = entrada * ingressoTotal
            print(f"Preço a pagar {pagamentoFinal}")
            codigoCartao = int(input("Digite o código do cartão: "))
            cvv = int(input("Digite o CVV: "))
        else:
            print("Não é uma opção")
            entrada = int(input("Tipo de ingresso: "))
            
        print("--------------------------") #ingresso
        
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        sorteio = random.choice(numeros)
        
        print("--------------------------") #ingresso
        print("🎟️INGRESSO🎟️")
        print(f"{nome}")
        print("Vingadores: Doutor Destino | 165 minutos")
        print(f"Sessão às 20:00 Cadeira:{cadeira} |Nº: {sorteio}")
        pergunta = input("Deseja adquirir outro ingresso?(Y/N): ")
        if pergunta == "Y" or pergunta == "y":
            filme = int(input("Escolha um filme: "))
        elif pergunta == "N" or pergunta == "n":
            print("Obrigao pela escolha!")
                    
        else:
            print("Não é uma opção")
            filme = int(input("Escolha um filme: "))
        print("--------------------------")
        
                
        print("--------------------------------------------------------------------------------------------------------") 
    
    elif filme == 2:
        print("Sessão do filme 'Os Farofeiros 3' às 16:00")
        print("Sessão de Segunda a Domingo")
        semana = input("Escolha o dia da semana: ")
        
        print("--------------------------") #quantidade
        
        ingressoTotal = int(input("Quantidades de ingressos: "))
        if ingressoTotal > 0 and ingressoTotal <= 20:
            print(f"Quantidade escolhida: {ingressoTotal}")
        else:
            print("Não é uma opção")
            entrada = input("Tipo de ingresso: ")
            
        print("--------------------------") #cadeira
        
        print("Escolha seu Assento(escolha uma opção disponivel): ")
        print("A1 | A2 | A3 | A4 | A5")
        print("B1 | B2 | B3 | B4 | B5")
        print("C1 | C2 | C3 | C4 | C5")
        print("D1 | D2 | D3 | D4 | D5")
        print("E1 | E2 | E3 | E4 | E5")
        if ingressoTotal != 1:
            cadeira = input("Selecione suas cadeiras: ")
        else:
            cadeira = input("Selecione sua cadeira: ")

        print("--------------------------") #ingresso meia ou inteira
        
        print("Tabela de preços")
        print("1- inteira: R$30,00")
        print("2- meia: R$15,00")
        entrada = int(input("Tipo de ingresso: "))
        if entrada == 1:
            entrada = 30
        elif entrada == 2:
            entrada = 15
        else:
            print("Não é uma opção")
            break
            entrada = input("Tipo de ingresso: ")
        
        print("--------------------------") #pagamento
        
        print("1- Pix")
        print("2- Cartão")
        pagamento = int(input("Escolha o tipo de pagamento: "))
        if pagamento == 1:
            nome = input("Digite seu nome: ") 
            pagamentoFinal = entrada * ingressoTotal
            print(f"Preço a pagar {pagamentoFinal}")
            print("Código pix: iytf@cvhgYf#fvRDcvbDV")
              
        elif pagamento == 2:
            nome = input("Digite seu nome: ")  
            pagamentoFinal = entrada * ingressoTotal
            print(f"Preço a pagar {pagamentoFinal}")
            codigoCartao = int(input("Digite o código do cartão: "))
            cvv = int(input("Digite o CVV: "))
        else:
            print("Não é uma opção")
            entrada = int(input("Tipo de ingresso: "))
            
        print("--------------------------") #ingresso
        
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        sorteio = random.choice(numeros)
        
        print("--------------------------") #ingresso
        print("🎟️INGRESSO🎟️")
        print(f"{nome}")
        print("Os Farofeiros 3 | 102 minutos")
        print(f"Sessão às 16:00 Cadeira:{cadeira} |Nº: {sorteio}")
        pergunta = input("Deseja adquirir outro ingresso?(Y/N): ")
        if pergunta == "Y" or pergunta == "y":
            filme = int(input("Escolha um filme: "))
        elif pergunta == "N" or pergunta == "n":
            print("Obrigao pela escolha!")
                    
        else:
            print("Não é uma opção")
            filme = int(input("Escolha um filme: "))
        print("--------------------------")
        
        print("--------------------------------------------------------------------------------------------------------") 
    
    elif filme == 3:
        print("Sessão do filme 'O Gatola Da Cartola' às 13:00")
        print("Sessão de Segunda a Domingo")
        semana = input("Escolha o dia da semana: ")
        
        print("--------------------------") #quantidade
        
        ingressoTotal = int(input("Quantidades de ingressos: "))
        if ingressoTotal > 0 and ingressoTotal <= 20:
            print(f"Quantidade escolhida: {ingressoTotal}")
        else:
            print("Não é uma opção")
            entrada = input("Tipo de ingresso: ")
            
        print("--------------------------") #cadeira
        
        print("Escolha seu Assento(escolha uma opção disponivel): ")
        print("A1 | A2 | A3 | A4 | A5")
        print("B1 | B2 | B3 | B4 | B5")
        print("C1 | C2 | C3 | C4 | C5")
        print("D1 | D2 | D3 | D4 | D5")
        print("E1 | E2 | E3 | E4 | E5")
        if ingressoTotal != 1:
            cadeira = input("Selecione suas cadeiras: ")
        else:
            cadeira = input("Selecione sua cadeira: ")

        print("--------------------------") #ingresso meia ou inteira
        
        print("Tabela de preços")
        print("1- inteira: R$30,00")
        print("2- meia: R$15,00")
        entrada = int(input("Tipo de ingresso: "))
        if entrada == 1:
            entrada = 30
        elif entrada == 2:
            entrada = 15
        else:
            print("Não é uma opção")
            break
            entrada = input("Tipo de ingresso: ")
        
        print("--------------------------") #pagamento
        
        print("1- Pix")
        print("2- Cartão")
        pagamento = int(input("Escolha o tipo de pagamento: "))
        if pagamento == 1:
            nome = input("Digite seu nome: ") 
            pagamentoFinal = entrada * ingressoTotal
            print(f"Preço a pagar {pagamentoFinal}")
            print("Código pix: iytf@cvhgYf#fvRDcvbDV")
              
        elif pagamento == 2:
            nome = input("Digite seu nome: ")  
            pagamentoFinal = entrada * ingressoTotal
            print(f"Preço a pagar {pagamentoFinal}")
            codigoCartao = int(input("Digite o código do cartão: "))
            cvv = int(input("Digite o CVV: "))
        else:
            print("Não é uma opção")
            entrada = int(input("Tipo de ingresso: "))
            
        print("--------------------------") #ingresso
        
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        sorteio = random.choice(numeros)
        
        print("--------------------------") #ingresso
        print("🎟️INGRESSO🎟️")
        print(f"{nome}")
        print("O Gatola Da Cartola | 114 minutos")
        print(f"Sessão às 13:00 Cadeira:{cadeira} |Nº: {sorteio}")
        pergunta = input("Deseja adquirir outro ingresso?(Y/N): ")
        if pergunta == "Y" or pergunta == "y":
            filme = int(input("Escolha um filme: "))
        elif pergunta == "N" or pergunta == "n":
            print("Obrigao pela escolha!")
            break
                    
        else:
            print("Não é uma opção")
            filme = int(input("Escolha um filme: "))
        print("--------------------------")
