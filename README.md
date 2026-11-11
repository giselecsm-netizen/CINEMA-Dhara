Solicitação do Cliente Cinema da Dhara.
Cliente 01 – Cinema DHARA.
A cinema precisa de um sistema que registre a venda dos ingressos de uma sessão.
Regras do sistema:
-  a sala é pequena apenas para 20 pessoas;
- Não pode vender mais que 20 ingressos disponíveis;
- Quando esgotar os ingressos informar que a sessão está lotada.

Desafio lógico. Como construir uma seqüência de decisões para verificar a situação de cada ingresso?
1) desafio, definir quanto tempo leva para desenvolver o programa?

2


P.O
2.hora para concluir a programação
rosi:20 min
manu:20 min
rafa:20 min
para realizar a programação


1 hora para concluir a programação

manu:20 min
rafaela:20 min
gisele:20 min 
naomy:20 min 

______ Analista  sistemas, Naomy e Gisele fizemos em nome da  Rose:

1- vai precisar de um menu com o titulo do filme, com a classificação indicativa do filme como LIVRE, como vai ser só uma sessão por enquanto, precisa de um horário inicial com tempo de duração do filme. exemplo do horário e duração: sessão às 19 horas com duração de 180 minutos .
o usuario seleciona e vai para o menu de valores, se valor de R$ inteira ou R$ meia entrada.

2 - também precisa colocar uma variável de escolha de assentos, com 5 fileiras com 5 cadeiras, (a1, a2, a3, a4, a5; proxima fileira B1 B2, B3,B4 e B5, e assim ate terminar os assentos). OBS: neste caso cria p input a pessoa seleciona entre as fileiras A,B,C,D E,  E OS NUMEROS, 1,2,3,4,5

3 - após selecionar o assento, vai para opção de pagamento, via pix (1) ou cartao de credito (2). a pessoa no menu escolhe o formato de pagamento, ao selecionar, por exemplo pix (1), vai para gerar o código pix e pagar, e se selecionar 2 cartao de credito, vai para preencher os dados do cartao de credito (neste caso um imput para dados, como nome, codigo do cartao, e numero CVV).

4- finalizado a compra, aparece no terminal com: parabéns compra realizada com sucesso, o nome do filme, a hora da sessão, e o assento do cinema.


>>>>>>>  ANALISTA ROSE<<<<<<<<

PARA OS INCREMENTOS A PETICAO DO CLIENTE PRECISAMOS: 
#REGISTAR NO SISTEMA UMA VARIAVEL QUE PERMIRA AO USUARIO DO CINEMA DIGITAR SEU NOME.
#CRIAR O MENU DOS FILMES 
#GERAR A QUANTIA DE BOLETOS QUE A PESSOA QUER COMPRAR NO SEU NOME
#O CLIENTE TEM A OPÇÃO DE ESCOLHER QUAIS POLTRONAS ELE GOSTARIA DE USAR, TERIA QUE APARECER PARA ELE AS QUE ESTÃO DISPONIVEIS.
# ALÉM DE TODAS AS PETICIONES ANTERIORES, AO FINALIZAR O PAGAMENTO PEDIR PARA: OK DO CLIENTE  E SE ELE DESEJA FAZER OUTRA COMPRA.
NOTA: BOM A UTILIZAR OPERADORES LOGICOS, NAO ESQUECER DE DECLARAR AS VARIAVEIS, QUANDO FINALIZAR A COMPRA NA OPCAO PIX OU CARTAO DE CREDITO, COM OS DADOS DO CARTAO. NA COMPRA FINALIZADA, TEM QUE APARECER O NOME DO CLIENTE, A QUANTIA DE INGRESOS, O NUMERO DA POLTRONA, O NOME DO FILME, O HORARIO DA SESSAO E DURACAO, POR ULTIMO PERGUNTAR SE ELE DESEJA FAZER OUTRA COMPRA.

TESTE:
 Quando iniciamos o sistema ele exibe a seguinte mensagem “🎥=CINEMA=🍿=
1 - Vingadores: Doutor Destino | 2h45
2 - Os Farofeiros 3 | 1h42
3 - O Gatola Da Cartola | 1h31
Escolha um filme:”
Se o usuário selecionar a opção “1”, a seguinte mensagem vai aparecer: “Sessão do filme 'Vingadores: Doutor Destino' às 20:00
Sessão de Segunda a Domingo
Escolha o dia da semana:” 
O usuário vai escolher um dia da semana, por exemplo, domingo. Em seguida vai aparecer a mensagem: “Quantidade de ingressos”, vamos por de exemplo, 3 ingressos. Após o sistema vai gerar a seguinte mensagem: “Escolha seu assento(escolha uma opção disponível):
A1 | A2 | A3 | A4 | A5
B1 | B2 | B3 | B4 | B5
C1 | C2 | C3 | C4 | C5
D1 | D2 | D3 | D4 | D5
E1 | E2 | E3 | E4 | E5
Selecione sua cadeira:”
O usuário vai selecionar três cadeiras, correspondente aos três ingressos que ele adquiriu. Vamos selecionar as cadeiras E1, E2 e E3. Após o sistema vai gerar a tabela de preços:
“Tabela de preços
inteira: R$30,00
meia: R$15,00
Tipo de ingresso:”
O usuário vai escolher se deseja um ingresso de inteira ou meia entrada. No exemplo foi escolhido a meia entrada. Após, o usuário vai escolher a forma de pagamento.
“1- Pix
2- Cartão
Escolha o tipo de pagamento:”
Se for selecionado a opção 1- Pix, o programa vai gerar a seguinte mensagem: “ Digite seu nome: “. Após ele vai gerar um código pix para ser pago, e vai gerar os ingressos com os dados cadastrados: 
“🎟️INGRESSO🎟️
Rafaela
Vingadores: Doutor Destino | 165 minutos
Cadeira:E1 E2 E3 | Nº: 8”

Se for selecionada a opção 2- Cartão, o programa vai gerar a seguinte mensagem: : “ Digite seu nome:
Digite o código do cartão:
Digite o CVV:”. Em seguida ele vai gerar os ingressos com os dados cadastrados: 
“🎟️INGRESSO🎟️
Rafaela
Vingadores: Doutor Destino | 165 minutos
Cadeira:E1 E2 E3 | Nº: 8”
Caso seja selecionada uma opção invalida o programa vai gerar a seguinte mensagem: “Não é uma opção”
Se forem selecionadas outras opções de filme, o programa vai seguir os mesmos passos do primeiro teste.
OBS: Faltou aparecer o dia da semana quando é gerado o ingresso.



