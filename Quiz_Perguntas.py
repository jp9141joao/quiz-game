import random
import os
import time


def Imprimir_Perguntas(Banco_Perguntas,Tema):
    
    Vidas = 3
    Acertos = 0
    Tam = len(Banco_Perguntas)
        
    while True:
        os.system('cls')
        Resp = input(f'\n* Quiz de {Tema} *\n\nVidas restantes: {Vidas}\n\nDigite "1" para começar\n\nR: ')
        
        Comecar = None
        
        if Resp.isdigit():
            Comecar = int(Resp)
        
        if Comecar is not None and Comecar == 1:
            break
    
    for Perg in Banco_Perguntas:
        
        if Vidas == 0:
            print('\nSuas vidas acabaram!')
            break
        
        while True:
            os.system('cls')
            print(f'\n* Quiz de {Tema} *\n\nVidas restantes: {Vidas}\n')
            print(f'{Perg["Pergunta"]}\n')
            
            for i, Opcao in enumerate(Perg['Opcao']):
                print(f'{i+1}) {Opcao}')
            
            Resp1 = input('\nR: ')
            
            Resp2 = None
            
            if Resp1.isdigit():
                Resp2 = int(Resp1)
                
            if Resp2 is not None and Resp2 > 0 and Resp2 <= len(Perg['Opcao']):
                break
        
        i = Resp2
        Resp2 = Perg['Opcao'][i-1]
        
        if Resp2 == Perg['Resposta']:
            Acertos += 1
            print('\nResposta correta!')
        else:
            Vidas -= 1
            print(f'\nResposta incorreta!')
            
        while True:
            Resp = input(f'\nDigite "1" para continuar\n\nR: ')
            
            Continuar = None
            
            if Resp.isdigit():
                Continuar = int(Resp)
            
            if Continuar is not None and Continuar == 1:
                break
            
    while True:
        os.system('cls')
        Resp = input(f'\nFim de jogo!\n\nNumero de acertos: {Acertos}\n\nDigite "1" para voltar\n\nR: ')
        
        Voltar = None
        
        if Resp.isdigit():
            Voltar = int(Resp)
        
        if Voltar is not None and Voltar == 1:
            break
            
                  
def Inicio():
    
    Banco_Geografia = [
        {
            'Pergunta': 'Quantos continentes existem no mundo?',
            'Opcao': ['Cinco','Seis','Sete','Oito'],
            'Resposta': 'Seis'
        },{
            'Pergunta': 'Qual o maior continente do mundo?',
            'Opcao': ['Asía','Europa','América do norte','Africa'],
            'Resposta': 'Asía'
        },{
            'Pergunta': 'Qual o menor continente do mundo?',
            'Opcao': ['America do norte','Oceania','Europa','Africa'],
            'Resposta': 'Oceania'
        },{
            'Pergunta': 'Qual o menor pais do mundo?',
            'Opcao': ['Vaticano','Mônaco','Tuvalu','San Marino'],
            'Resposta': 'Vaticano'
        },{
            'Pergunta': 'Qual o país com a maior população do mundo?',
            'Opcao': ['Estados Unidos','India','Russia','China'],
            'Resposta': 'China'
        },{
            'Pergunta': 'Quantos paises existem na américa do norte?',
            'Opcao': ['Dois','Três','Quatro','Cinco'],
            'Resposta': 'Três'
        },{
            'Pergunta': 'Qual o país mais rico da europa?',
            'Opcao': ['Inglaterra','Bulgária','Luxemburgo','Romênia'],
            'Resposta': 'Luxemburgo'
        },{
            'Pergunta': 'Qual o país mais quente do mundo?',
            'Opcao': ['Sudão','Libia','Zambia','Mali'],
            'Resposta': 'Mali'
        },{
            'Pergunta': 'Quantos estados existem no brasil?',
            'Opcao': ['Vinte e cinco','Vinte e sete','Vinte e dois','Vinte e seis'],
            'Resposta': 'Vinte e seis'
        },{
            'Pergunta': 'Qual a população do brasil?',
            'Opcao': ['211 milhões','214 milhões','221 milhões','225 milhões'],
            'Resposta': '214 milhões'
        },{
            'Pergunta': 'Qual dessas já foi capital do brasil?',
            'Opcao': ['Belo Horizonte','Fortaleza','Rio grande do sul','Salvador'],
            'Resposta': 'Salvador'
        },{
            'Pergunta': 'Qual o país mais pobre do mundo?',
            'Opcao': ['Uganda','Congo','Nigéria','Zimbabué'],
            'Resposta': 'Zimbabué'
        },{
            'Pergunta': 'Quantos oceanos existem no mundo?',
            'Opcao': ['Três','Quatro','Cinco','Seis'],
            'Resposta': 'Quatro'
        },{
            'Pergunta': 'Qual o país mais frio do mundo?',
            'Opcao': ['Russia','Antartida','Canadá','Escócia'],
            'Resposta': 'Antartida'
        },{
            'Pergunta': 'Qual a cidade mais populosa do mundo?',
            'Opcao': ['São Paulo','Nova deli','Toquio','Xangai'],
            'Resposta': 'Toquio'
        },{
            'Pergunta': 'Qual o lugar mais alto do brasil?',
            'Opcao': ['Pico da neblina','Pico da bandeira','Pico do calçado','Pico pedra da mina'],
            'Resposta': 'Pico da neblina'
        },{
            'Pergunta': 'Qual o país mais rico do mundo?',
            'Opcao': ['Inglaterra','China','Estados Unidos','Emirados Arabes'],
            'Resposta': 'Estados Unidos'
        }
    ]
    
    Banco_Biologia = [
        {
            'Pergunta': 'Qual o maior animal do mundo?',
            'Opcao':['Baleia azul','Elefante','Lula gigante','Tubarão baleia'],
            'Resposta': 'Baleia azul'
        },{
            'Pergunta': 'Qual o animal mais rapido do mundo?',
            'Opcao':['Guepardo','Falcão','Águia','Leopardo'],
            'Resposta': 'Falcão'
        },{
            'Pergunta': 'Qual animal pode sobreviver ao espaço?',
            'Opcao':['Barata','Urso da água','Vespa africana','Formiga fantasma'],
            'Resposta': 'Urso da água'    
        },{
            'Pergunta': 'Qual o animal mais venenoso do mundo?',
            'Opcao':['Largato dragão de komodo','Cobra Mamba negra','Água viva caça-fantasma','Peixe pedra'],
            'Resposta': 'Água viva caça-fantasma'
        },{
            'Pergunta': 'Qual o animal mais inteligente do mundo?',
            'Opcao':['Chimpanzé','Golfinho','Border Collie','Polvo'],
            'Resposta': 'Golfinho'
        },{
            'Pergunta': 'Qual animal pode viver para sempre?',
            'Opcao': ['Água viva','Tartaruga','Vírus','Barata'],
            'Resposta': 'Água viva'   
        },{
            'Pergunta': 'Qual animal possui a mordida mais forte?',
            'Opcao': ['Crocodilo','Leão','Tigre','Hipopótamo'],
            'Resposta': 'Hipopótamo'
        },{
            'Pergunta': 'Qual o animal que mais usa a sua capacidade cerebral?',
            'Opcao': ['Humano','Golfinho','Chimpanzé','Polvo'],
            'Resposta': 'Golfinho'
        },{
            'Pergunta': 'Qual destes animais existe a mais tempo na terra?',
            'Opcao': ['Tubarão','Polvo','Lula','Caranguejo'],
            'Resposta': 'Tubarão'
        },{
            'Pergunta': 'Qual o maior orgão do corpo humano?',
            'Opcao': ['Cerebro','Figado','Intestino Delgado','Pele'],
            'Resposta': 'Pele'
        },{
            'Pergunta': 'Qual o maior musculo do corpo humano?',
            'Opcao': ['Lingua','Quadriceps','Dorsal','Biceps'],
            'Resposta': 'Lingua'
        },{
            'Pergunta': 'Qual o unico mamifero voador no mundo?',
            'Opcao': ['Àguia','Pavão','Morcego','Garsa'],
            'Resposta': ''
        },{
            'Pergunta': 'Qual o unico mamifero que bota ovos?',
            'Opcao': ['Ornitorrinco','Leão do mar','Cobra','Peixe boi'],
            'Resposta': 'Ornitorrinco'
        },{
            'Pergunta': 'Qual a cor do pelo do urso polar?',
            'Opcao': ['Branca','Cinza','Preta','Transparente'],
            'Resposta': 'Transparente'
        },{
            'Pergunta': 'Saliva de qual animal possui propriedades antisséptica?',
            'Opcao': ['Cão','Gato','Macaco','Tigre'],
            'Resposta': 'Tigre'
        },{
            'Pergunta': 'Qual tempo maximo que o corpo humano aguenta sem água?',
            'Opcao': ['2 dias','3 dias','4 dias','1 semana'],
            'Resposta': '1 semana'
        }
    ]
    
    Banco_Jogos = [
        {
            'Pergunta': 'Qual o jogo mais vendido de todos os tempos?',
            'Opcao':['Mario','Tetris','Gta 5','Minecraft'],
            'Resposta': 'Minecraft'
        },{
            'Pergunta': 'Quando foi lançado o primeiro video game do mundo?',
            'Opcao':['1980','1975','1972','1983'],
            'Resposta': '1972'
        },{
            'Pergunta': 'Qual foi o primeiro jogo criado no mundo?',
            'Opcao':['Jogo da velha','Tenis','Jogo dos erros','Ping pong'],
            'Resposta': 'Tenis'
        },{
            'Pergunta': 'Qual o jogo com maior mapa aberto da historia?',
            'Opcao':['No mens sky','Gta 5','Fortnite','Dinow mendes sky'],
            'Resposta': 'Dinow mendes sky'
        },{
            'Pergunta': 'Qual o jogo mais jogado de todos os tempos?',
            'Opcao':['Minecraft','Tetris','Gta','Fortnite'],
            'Resposta': 'Minecraft'
        },{
            'Pergunta': 'Qual o jogo teve o maior numero de copias vendidas em menos de 24 horas?',
            'Opcao':['Gta 5','Minecraft','Call of duty 3','Mario kart'],
            'Resposta': 'Gta 5'
        },{
            'Pergunta': 'Qual foi o primeiro video game lançado no mundo',
            'Opcao':['Magnavox Odyssey','Playstation','Atari','Nitendo'],
            'Resposta': 'Magnavox Odyssey'
        },{
            'Pergunta': 'Qual o jogo de luta mais famoso de todos os tempos?',
            'Opcao':['Mortal Kombat','Street fighter','Jump force','Super smash bros'],
            'Resposta': 'Mortal Kombat'
        },{
            'Pergunta': 'Qual o jogo mais pesado da atualidade?',
            'Opcao':['Final Fantasy XV','Call of duty black ops 4','No mans sky','Battlefield'],
            'Resposta': 'Final Fantasy XV'
        },{
            'Pergunta': 'Qual o jogo mais jogado no playstation da atualidade?',
            'Opcao':['The last of us','Fortnite','Call of duty warzone','Rainbow six'],
            'Resposta': 'Fortnite'
        },{
            'Pergunta': 'Qual o jogo mais jogado no xbox da atualidade?',
            'Opcao':['The last of us','Fortnite','Call of duty warzone','Rainbow six'],
            'Resposta': 'Fortnite'
        },{
            'Pergunta': 'Qual é o console mais vendido de todos os tempos?',
            'Opcao':['Nitendo DS','PS4','Game boy','PS2'],
            'Resposta': 'PS2'
        },{
            'Pergunta': 'Qual o jogo de corrida mais vendido no mundo?',
            'Opcao':['Gran turismo','Forza horyzon','Mario kart','Need for speed'],
            'Resposta': 'Mario kart'
        },{
            'Pergunta': 'Qual o jogo mais vendido da nitendo?',
            'Opcao':['The Legend of Zelda','Mario kart','Pokemon','Super mario bros'],
            'Resposta': 'The Legend of Zelda'
        }
    ]
    
    Banco_Filmes_Series = [
        {
            'Pergunta': 'Qual o filme de maior bilheteria de todos os tempos?',
            'Opcao': ['Titanic','Avatar 2','Vingadores ultimato','Avatar 1'],
            'Resposta': 'Avatar 1'
        },{
            'Pergunta': 'Qual o filme com mais indicações ao oscar?',
            'Opcao': ['Oppenheimer','O regresso','Titanic','No limite do amanha'],
            'Resposta': 'Titanic'
        },{
            'Pergunta': 'Quando foi exibido o primeiro filme da historia?',
            'Opcao': ['1895','1914','1901','1933'],
            'Resposta': '1895'
        },{
            'Pergunta': 'Onde foi exibido o primeiro filme da historia?',
            'Opcao': ['Lisboa','Madrid','Londres','Paris'],
            'Resposta': 'Paris'
        },{
            'Pergunta': 'Qual o filme com maior numero de oscar da atualiadade?',
            'Opcao': ['Avatar 1','Titanic','Coringa','Senhor dos aneis'],
            'Resposta': 'Titanic'
        },{
            'Pergunta': 'Qual a serie com mais temporadas da atualidade?',
            'Opcao': ['Supernatural','Greys anatomy','Simpsons','South Park'],
            'Resposta': 'Simpsons'
        },{
            'Pergunta': 'Qual a serie com maior numero de episodios da historia?',
            'Opcao': ['Doctor who','Simpsons','Futurama','Tom e jerry'],
            'Resposta': 'Doctor who'
        },{
            'Pergunta': 'Qual o maior filme da historia?',
            'Opcao': ['The Cure for Insomnia','The Longest Most Meaningless Movie in the World','Justice league','Four Stars'],
            'Resposta': 'The Cure for Insomnia'
        },{
            'Pergunta': 'Qual o menor filme da historia?',
            'Opcao': ['La Jetée','Elevator Movie','Un Chien Andalou','A Boy and His Atom'],
            'Resposta': 'A Boy and His Atom'
        },{
            'Pergunta': 'Qual o filme que ficou mais tempo em cartaz?',
            'Opcao': ['Planeta dos macacos 1','Liga da justiça','Vingadores ultimato','Titanic'],
            'Resposta': 'Vingadores ultimato'
        },{
            'Pergunta': 'Qual diretor possui mais filmes no top 5 maiores bilheterias do mundo?',
            'Opcao': ['James Cameron','Alejandro González','James Gunn','Zack Snyder'],
            'Resposta': 'James Cameron'
        },{
            'Pergunta': 'Qual a serie que mais gastou por episodeo no mundo?',
            'Opcao': ['Game of thrones','O senhor dos anéis: Os Anéis de Poder','Stranger things','Wanda vision'],
            'Resposta': 'O senhor dos anéis: Os Anéis de Poder'
        }
    ]
    
    while True:
        os.system('cls')
        Resp = input('\n* Menu do Quiz *\n\n1- Quiz de Geografia\n2- Quiz de Biologia\n3- Quiz de Jogos\n4- Quiz de Filmes e Series\n5- Sair\n\nR: ')
        
        Menu = None
        
        if Resp.isdigit():
            Menu = int(Resp)
            
        if Menu is not None:
            if Menu == 5:
                print('\nQuiz encerrado!')
                break
            elif Menu == 1:
                Imprimir_Perguntas(Banco_Geografia,'Geografia')
            elif Menu == 2:
                Imprimir_Perguntas(Banco_Biologia,'Biologia')
            elif Menu == 3:
                Imprimir_Perguntas(Banco_Jogos,'Jogos')
            elif Menu == 4:
                Imprimir_Perguntas(Banco_Filmes_Series,'Filmes e Series')
            else:
                while True:
                    os.system('cls')
                    Resp = input('\nOpção invalida!\n\nDigite "1" para voltar\n\nR: ')
                    
                    Voltar = None                    
                    
                    if Resp.isdigit():
                        Voltar = int(Resp)
                        
                    if Voltar is not None and Voltar == 1:
                        break
                
                  
Inicio()